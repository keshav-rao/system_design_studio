# Probabilistic data types

```json metadata
{
  "schema_version": 2,
  "title": "Probabilistic data types",
  "description": "Learn how to use approximate calculations with Redis.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"children":[{"id":"set-membership","title":"Set membership"},{"id":"set-cardinality","title":"Set cardinality"}],"id":"set-operations","title":"Set operations"},{"children":[{"id":"frequency","title":"Frequency"},{"id":"quantiles","title":"Quantiles"},{"id":"ranking","title":"Ranking"}],"id":"statistics","title":"Statistics"}]}

,
  "codeExamples": [{"codetabsId":"home_prob_dts-stepbloom","description":"Foundational: Use Bloom filters for memory-efficient set membership testing with false positive possibility","difficulty":"beginner","id":"bloom","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_home_prob_dts-stepbloom"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_home_prob_dts-stepbloom"}]},{"codetabsId":"home_prob_dts-stepcuckoo","description":"Foundational: Use Cuckoo filters for set membership testing with deletion support and faster lookups than Bloom filters","difficulty":"beginner","id":"cuckoo","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_home_prob_dts-stepcuckoo"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_home_prob_dts-stepcuckoo"}]},{"codetabsId":"home_prob_dts-stephyperloglog","description":"Foundational: Estimate set cardinality with HyperLogLog for memory-efficient counting of distinct items","difficulty":"beginner","id":"hyperloglog","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_home_prob_dts-stephyperloglog"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_home_prob_dts-stephyperloglog"}]},{"codetabsId":"home_prob_dts-stepcms","description":"Foundational: Track approximate item frequencies with Count-min sketch for memory-efficient statistics on data streams","difficulty":"intermediate","id":"cms","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_home_prob_dts-stepcms"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_home_prob_dts-stepcms"}]},{"codetabsId":"home_prob_dts-steptdigest","description":"Foundational: Estimate quantiles and percentiles with t-digest for memory-efficient statistical analysis of large datasets","difficulty":"intermediate","id":"tdigest","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_home_prob_dts-steptdigest"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_home_prob_dts-steptdigest"}]},{"codetabsId":"home_prob_dts-steptopk","description":"Foundational: Track top K most frequent items in a data stream with Top-K for efficient ranking without storing all items","difficulty":"intermediate","id":"topk","languages":[{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_home_prob_dts-steptopk"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_home_prob_dts-steptopk"}]}]
}
```

## Code Examples Legend

The code examples below show how to perform the same operations in different programming languages and client libraries:

- **Redis CLI**: Command-line interface for Redis
- **C# (Synchronous)**: StackExchange.Redis synchronous client
- **C# (Asynchronous)**: StackExchange.Redis asynchronous client
- **Go**: go-redis client
- **Java (Synchronous - Jedis)**: Jedis synchronous client
- **Java (Asynchronous - Lettuce)**: Lettuce asynchronous client
- **Java (Reactive - Lettuce)**: Lettuce reactive/streaming client
- **JavaScript (Node.js)**: node-redis client
- **PHP**: Predis client
- **Python**: redis-py client
- **Rust (Synchronous)**: redis-rs synchronous client
- **Rust (Asynchronous)**: redis-rs asynchronous client

Each code example demonstrates the same basic operation across different languages. The specific syntax and patterns vary based on the language and client library, but the underlying Redis commands and behavior remain consistent.

---


Redis supports several
[probabilistic data types](https://redis.io/docs/latest/develop/data-types/probabilistic)
that let you calculate values approximately rather than exactly.
The types fall into two basic categories:

-   [Set operations](#set-operations): These types let you calculate (approximately)
    the number of items in a set of distinct values, and whether or not a given value is
    a member of a set.
-   [Statistics](#statistics): These types give you an approximation of
    statistics such as the quantiles, ranks, and frequencies of numeric data points in
    a list.

To see why these approximate calculations would be useful, consider the task of
counting the number of distinct IP addresses that access a website in one day.

Assuming that you already have code that supplies you with each IP
address as a string, you could record the addresses in Redis using
a [set](https://redis.io/docs/latest/develop/data-types/sets):

```java
commands.sadd("ip_tracker", newIpAddress);
```

The set can only contain each key once, so if the same address
appears again during the day, the new instance will not change
the set. At the end of the day, you could get the exact number of
distinct addresses using the `scard()` method:

```java
RedisFuture<Long> numDistinctIps = commands.scard("ip_tracker");
```

This approach is simple, effective, and precise but if your website
is very busy, the `ip_tracker` set could become very large and consume
a lot of memory.

You would probably round the count of distinct IP addresses to the
nearest thousand or more to deliver the usage statistics, so
getting it exactly right is not important. It would be useful
if you could trade off some accuracy in exchange for lower memory
consumption. The probabilistic data types provide exactly this kind of
trade-off. Specifically, you can count the approximate number of items in a
set using the [HyperLogLog](#set-cardinality) data type, as described below.

In general, the probabilistic data types let you perform approximations with a
bounded degree of error that have much lower memory consumption or execution
time than the equivalent precise calculations.

The examples below use the asynchronous and reactive command APIs, but the
probabilistic commands are also available through the synchronous API. You can
access all of these commands directly from the standard Lettuce command
interfaces (for example, `RedisAsyncCommands` or `RedisReactiveCommands`),
just like the core Redis commands.

## Set operations

Redis supports the following approximate set operations:

-   [Membership](#set-membership): The
    [Bloom filter](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter) and
    [Cuckoo filter](https://redis.io/docs/latest/develop/data-types/probabilistic/cuckoo-filter)
    data types let you track whether or not a given item is a member of a set.
-   [Cardinality](#set-cardinality): The
    [HyperLogLog](https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs)
    data type gives you an approximate value for the number of items in a set, also
    known as the *cardinality* of the set.

The sections below describe these operations in more detail.

### Set membership

[Bloom filter](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter) and
[Cuckoo filter](https://redis.io/docs/latest/develop/data-types/probabilistic/cuckoo-filter)
objects provide a set membership operation that lets you track whether or not a
particular item has been added to a set. These two types provide different
trade-offs for memory usage and speed, so you can select the best one for your
use case. Note that for both types, there is an asymmetry between presence and
absence of items in the set. If an item is reported as absent, then it is definitely
absent, but if it is reported as present, then there is a small chance it may really be
absent.

Instead of storing strings directly, like a [set](https://redis.io/docs/latest/develop/data-types/sets),
a Bloom filter records the presence or absence of the
[hash value](https://en.wikipedia.org/wiki/Hash_function) of a string.
This gives a very compact representation of the
set's membership with a fixed memory size, regardless of how many items you
add. The following example adds some names to a Bloom filter representing
a list of users and checks for the presence or absence of users in the list.

Foundational: Use Bloom filters for memory-efficient set membership testing with false positive possibility

**Difficulty:** Beginner

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> bloomExample = asyncCommands
                    .bfMAdd("recorded_users", "andy", "cameron", "david", "michelle")
                    .thenCompose(res1 -> {
                        System.out.println(res1);
                        // >>> [true, true, true, true]
                        return asyncCommands.bfExists("recorded_users", "cameron");
                    })
                    .thenCompose(res2 -> {
                        System.out.println(res2);
                        // >>> true
                        return asyncCommands.bfExists("recorded_users", "kaitlyn");
                    })
                    .thenAccept(res3 -> {
                        System.out.println(res3);
                        // >>> false
                    })
                    .toCompletableFuture();

            bloomExample.join();
```

##### Java (Reactive - Lettuce)

```java
            List<Boolean> res1 = reactiveCommands
                    .bfMAdd("recorded_users", "andy", "cameron", "david", "michelle")
                    .map(Value::getValue)
                    .collectList()
                    .block();
            System.out.println(res1);
            // >>> [true, true, true, true]

            Boolean res2 = reactiveCommands.bfExists("recorded_users", "cameron").block();
            System.out.println(res2);
            // >>> true

            Boolean res3 = reactiveCommands.bfExists("recorded_users", "kaitlyn").block();
            System.out.println(res3);
            // >>> false
```



A Cuckoo filter has similar features to a Bloom filter, but also supports
a deletion operation to remove hashes from a set, as shown in the example
below.

Foundational: Use Cuckoo filters for set membership testing with deletion support and faster lookups than Bloom filters

**Difficulty:** Beginner

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> cuckooExample = asyncCommands
                    .cfAdd("other_users", "paolo")
                    .thenCompose(res4 -> {
                        System.out.println(res4);
                        // >>> true
                        return asyncCommands.cfAdd("other_users", "kaitlyn");
                    })
                    .thenCompose(res5 -> {
                        System.out.println(res5);
                        // >>> true
                        return asyncCommands.cfAdd("other_users", "rachel");
                    })
                    .thenCompose(res6 -> {
                        System.out.println(res6);
                        // >>> true
                        return asyncCommands.cfMExists("other_users", "paolo", "rachel", "andy");
                    })
                    .thenCompose(res7 -> {
                        System.out.println(res7);
                        // >>> [true, true, false]
                        return asyncCommands.cfDel("other_users", "paolo");
                    })
                    .thenCompose(res8 -> {
                        System.out.println(res8);
                        // >>> true
                        return asyncCommands.cfExists("other_users", "paolo");
                    })
                    .thenAccept(res9 -> {
                        System.out.println(res9);
                        // >>> false
                    })
                    .toCompletableFuture();

            cuckooExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Boolean res4 = reactiveCommands.cfAdd("other_users", "paolo").block();
            System.out.println(res4);
            // >>> true

            Boolean res5 = reactiveCommands.cfAdd("other_users", "kaitlyn").block();
            System.out.println(res5);
            // >>> true

            Boolean res6 = reactiveCommands.cfAdd("other_users", "rachel").block();
            System.out.println(res6);
            // >>> true

            List<Boolean> res7 = reactiveCommands
                    .cfMExists("other_users", "paolo", "rachel", "andy")
                    .collectList()
                    .block();
            System.out.println(res7);
            // >>> [true, true, false]

            Boolean res8 = reactiveCommands.cfDel("other_users", "paolo").block();
            System.out.println(res8);
            // >>> true

            Boolean res9 = reactiveCommands.cfExists("other_users", "paolo").block();
            System.out.println(res9);
            // >>> false
```



Which of these two data types you choose depends on your use case.
Bloom filters are generally faster than Cuckoo filters when adding new items,
and also have better memory usage. Cuckoo filters are generally faster
at checking membership and also support the delete operation. See the
[Bloom filter](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter) and
[Cuckoo filter](https://redis.io/docs/latest/develop/data-types/probabilistic/cuckoo-filter)
reference pages for more information and comparison between the two types.

### Set cardinality

A [HyperLogLog](https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs)
object calculates the cardinality of a set. As you add
items, the HyperLogLog tracks the number of distinct set members but
doesn't let you retrieve them or query which items have been added.
You can also merge two or more HyperLogLogs to find the cardinality of the
[union](https://en.wikipedia.org/wiki/Union_(set_theory)) of the sets they
represent.

Foundational: Estimate set cardinality with HyperLogLog for memory-efficient counting of distinct items

**Difficulty:** Beginner

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> hllExample = asyncCommands
                    .pfadd("group:1", "andy", "cameron", "david")
                    .thenCompose(res10 -> {
                        System.out.println(res10);
                        // >>> 1
                        return asyncCommands.pfcount("group:1");
                    })
                    .thenCompose(res11 -> {
                        System.out.println(res11);
                        // >>> 3
                        return asyncCommands.pfadd("group:2", "kaitlyn", "michelle", "paolo", "rachel");
                    })
                    .thenCompose(res12 -> {
                        System.out.println(res12);
                        // >>> 1
                        return asyncCommands.pfcount("group:2");
                    })
                    .thenCompose(res13 -> {
                        System.out.println(res13);
                        // >>> 4
                        return asyncCommands.pfmerge("both_groups", "group:1", "group:2");
                    })
                    .thenCompose(res14 -> {
                        System.out.println(res14);
                        // >>> OK
                        return asyncCommands.pfcount("both_groups");
                    })
                    .thenAccept(res15 -> {
                        System.out.println(res15);
                        // >>> 7
                    })
                    .toCompletableFuture();

            hllExample.join();
```

##### Java (Reactive - Lettuce)

```java
            Long res10 = reactiveCommands.pfadd("group:1", "andy", "cameron", "david").block();
            System.out.println(res10);
            // >>> 1

            Long res11 = reactiveCommands.pfcount("group:1").block();
            System.out.println(res11);
            // >>> 3

            Long res12 = reactiveCommands.pfadd("group:2", "kaitlyn", "michelle", "paolo", "rachel").block();
            System.out.println(res12);
            // >>> 1

            Long res13 = reactiveCommands.pfcount("group:2").block();
            System.out.println(res13);
            // >>> 4

            String res14 = reactiveCommands.pfmerge("both_groups", "group:1", "group:2").block();
            System.out.println(res14);
            // >>> OK

            Long res15 = reactiveCommands.pfcount("both_groups").block();
            System.out.println(res15);
            // >>> 7
```



The main benefit that HyperLogLogs offer is their very low
memory usage. They can count up to 2^64 items with less than
1% standard error using a maximum 12KB of memory. This makes
them very useful for counting things like the total of distinct
IP addresses that access a website or the total of distinct
bank card numbers that make purchases within a day.

## Statistics

Redis supports several approximate statistical calculations
on numeric data sets:

-   [Frequency](#frequency): The
    [Count-min sketch](https://redis.io/docs/latest/develop/data-types/probabilistic/count-min-sketch)
    data type lets you find the approximate frequency of a labeled item in a data stream.
-   [Quantiles](#quantiles): The
    [t-digest](https://redis.io/docs/latest/develop/data-types/probabilistic/t-digest)
    data type estimates the quantile of a query value in a data stream.
-   [Ranking](#ranking): The
    [Top-K](https://redis.io/docs/latest/develop/data-types/probabilistic/top-k) data type
    estimates the ranking of labeled items by frequency in a data stream.

The sections below describe these operations in more detail.

### Frequency

A [Count-min sketch](https://redis.io/docs/latest/develop/data-types/probabilistic/count-min-sketch)
(CMS) object keeps count of a set of related items represented by
string labels. The count is approximate, but you can specify
how close you want to keep the count to the true value (as a fraction)
and the acceptable probability of failing to keep it in this
desired range. For example, you can request that the count should
stay within 0.1% of the true value and have a 0.05% probability
of going outside this limit. The example below shows how to create
a Count-min sketch object, add data to it, and then query it.

Foundational: Track approximate item frequencies with Count-min sketch for memory-efficient statistics on data streams

**Difficulty:** Intermediate

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> cmsExample = asyncCommands
                    // Specify that you want to keep the counts within 0.01
                    // (1%) of the true value with a 0.005 (0.5%) chance
                    // of going outside this limit.
                    .cmsInitByProb("items_sold", 0.01, 0.005)
                    .thenCompose(res16 -> {
                        System.out.println(res16);
                        // >>> OK
                        return asyncCommands.cmsIncrBy("items_sold",
                                IncrementPair.of("bread", 300L),
                                IncrementPair.of("tea", 200L),
                                IncrementPair.of("coffee", 200L),
                                IncrementPair.of("beer", 100L));
                    })
                    .thenCompose(res17 -> {
                        List<Long> sorted17 = new ArrayList<>(res17);
                        sorted17.sort(null);
                        System.out.println(sorted17);
                        // >>> [100, 200, 200, 300]
                        return asyncCommands.cmsIncrBy("items_sold",
                                IncrementPair.of("bread", 100L),
                                IncrementPair.of("coffee", 150L));
                    })
                    .thenCompose(res18 -> {
                        List<Long> sorted18 = new ArrayList<>(res18);
                        sorted18.sort(null);
                        System.out.println(sorted18);
                        // >>> [350, 400]
                        return asyncCommands.cmsQuery("items_sold", "bread", "tea", "coffee", "beer");
                    })
                    .thenAccept(res19 -> {
                        List<Long> sorted19 = new ArrayList<>(res19);
                        sorted19.sort(null);
                        System.out.println(sorted19);
                        // >>> [100, 200, 350, 400]
                    })
                    .toCompletableFuture();

            cmsExample.join();
```

##### Java (Reactive - Lettuce)

```java
            // Specify that you want to keep the counts within 0.01
            // (1%) of the true value with a 0.005 (0.5%) chance
            // of going outside this limit.
            String res16 = reactiveCommands.cmsInitByProb("items_sold", 0.01, 0.005).block();
            System.out.println(res16);
            // >>> OK

            List<Long> res17 = new ArrayList<>(reactiveCommands
                    .cmsIncrBy("items_sold",
                            IncrementPair.of("bread", 300L),
                            IncrementPair.of("tea", 200L),
                            IncrementPair.of("coffee", 200L),
                            IncrementPair.of("beer", 100L))
                    .collectList()
                    .block());
            res17.sort(null);
            System.out.println(res17);
            // >>> [100, 200, 200, 300]

            List<Long> res18 = new ArrayList<>(reactiveCommands
                    .cmsIncrBy("items_sold",
                            IncrementPair.of("bread", 100L),
                            IncrementPair.of("coffee", 150L))
                    .collectList()
                    .block());
            res18.sort(null);
            System.out.println(res18);
            // >>> [350, 400]

            List<Long> res19 = new ArrayList<>(reactiveCommands
                    .cmsQuery("items_sold", "bread", "tea", "coffee", "beer")
                    .collectList()
                    .block());
            res19.sort(null);
            System.out.println(res19);
            // >>> [100, 200, 350, 400]
```



The advantage of using a CMS over keeping an exact count with a
[sorted set](https://redis.io/docs/latest/develop/data-types/sorted-sets)
is that that a CMS has very low and fixed memory usage, even for
large numbers of items. Use CMS objects to keep daily counts of
items sold, accesses to individual web pages on your site, and
other similar statistics.

### Quantiles

A [quantile](https://en.wikipedia.org/wiki/Quantile) is the value
below which a certain fraction of samples lie. For example, with
a set of measurements of people's heights, the quantile of 0.75 is
the value of height below which 75% of all people's heights lie.
[Percentiles](https://en.wikipedia.org/wiki/Percentile) are equivalent
to quantiles, except that the fraction is expressed as a percentage.

A [t-digest](https://redis.io/docs/latest/develop/data-types/probabilistic/t-digest)
object can estimate quantiles from a set of values added to it
without having to store each value in the set explicitly. This can
save a lot of memory when you have a large number of samples.

The example below shows how to add data samples to a t-digest
object and obtain some basic statistics, such as the minimum and
maximum values, the quantile of 0.75, and the
[cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function)
(CDF), which is effectively the inverse of the quantile function. It also
shows how to merge two or more t-digest objects to query the combined
data set.

Foundational: Estimate quantiles and percentiles with t-digest for memory-efficient statistical analysis of large datasets

**Difficulty:** Intermediate

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> tdigestExample = asyncCommands
                    .tdigestCreate("male_heights")
                    .thenCompose(res20 -> {
                        System.out.println(res20);
                        // >>> OK
                        return asyncCommands.tdigestAdd("male_heights",
                                175.5, 181, 160.8, 152, 177, 196, 164);
                    })
                    .thenCompose(res21 -> {
                        System.out.println(res21);
                        // >>> OK
                        return asyncCommands.tdigestMin("male_heights");
                    })
                    .thenCompose(res22 -> {
                        System.out.println(res22);
                        // >>> 152.0
                        return asyncCommands.tdigestMax("male_heights");
                    })
                    .thenCompose(res23 -> {
                        System.out.println(res23);
                        // >>> 196.0
                        return asyncCommands.tdigestQuantile("male_heights", 0.75);
                    })
                    .thenCompose(res24 -> {
                        System.out.println(res24);
                        // >>> [181.0]
                        // Note that the CDF value for 181 is not exactly 0.75.
                        // Both values are estimates.
                        return asyncCommands.tdigestCDF("male_heights", 181);
                    })
                    .thenCompose(res25 -> {
                        System.out.println(res25);
                        // >>> [0.7857142857142857]
                        return asyncCommands.tdigestCreate("female_heights");
                    })
                    .thenCompose(res26 -> {
                        System.out.println(res26);
                        // >>> OK
                        return asyncCommands.tdigestAdd("female_heights",
                                155.5, 161, 168.5, 170, 157.5, 163, 171);
                    })
                    .thenCompose(res27 -> {
                        System.out.println(res27);
                        // >>> OK
                        return asyncCommands.tdigestQuantile("female_heights", 0.75);
                    })
                    .thenCompose(res28 -> {
                        System.out.println(res28);
                        // >>> [170.0]
                        return asyncCommands.tdigestMerge("all_heights", "male_heights", "female_heights");
                    })
                    .thenCompose(res29 -> {
                        System.out.println(res29);
                        // >>> OK
                        return asyncCommands.tdigestQuantile("all_heights", 0.75);
                    })
                    .thenAccept(res30 -> {
                        System.out.println(res30);
                        // >>> [175.5]
                    })
                    .toCompletableFuture();

            tdigestExample.join();
```

##### Java (Reactive - Lettuce)

```java
            String res20 = reactiveCommands.tdigestCreate("male_heights").block();
            System.out.println(res20);
            // >>> OK

            String res21 = reactiveCommands.tdigestAdd("male_heights",
                    175.5, 181, 160.8, 152, 177, 196, 164).block();
            System.out.println(res21);
            // >>> OK

            Double res22 = reactiveCommands.tdigestMin("male_heights").block();
            System.out.println(res22);
            // >>> 152.0

            Double res23 = reactiveCommands.tdigestMax("male_heights").block();
            System.out.println(res23);
            // >>> 196.0

            List<Double> res24 = reactiveCommands.tdigestQuantile("male_heights", 0.75)
                    .collectList().block();
            System.out.println(res24);
            // >>> [181.0]

            // Note that the CDF value for 181 is not exactly 0.75.
            // Both values are estimates.
            List<Double> res25 = reactiveCommands.tdigestCDF("male_heights", 181)
                    .collectList().block();
            System.out.println(res25);
            // >>> [0.7857142857142857]

            String res26 = reactiveCommands.tdigestCreate("female_heights").block();
            System.out.println(res26);
            // >>> OK

            String res27 = reactiveCommands.tdigestAdd("female_heights",
                    155.5, 161, 168.5, 170, 157.5, 163, 171).block();
            System.out.println(res27);
            // >>> OK

            List<Double> res28 = reactiveCommands.tdigestQuantile("female_heights", 0.75)
                    .collectList().block();
            System.out.println(res28);
            // >>> [170.0]

            String res29 = reactiveCommands.tdigestMerge("all_heights", "male_heights", "female_heights").block();
            System.out.println(res29);
            // >>> OK

            List<Double> res30 = reactiveCommands.tdigestQuantile("all_heights", 0.75)
                    .collectList().block();
            System.out.println(res30);
            // >>> [175.5]
```



A t-digest object also supports several other related commands, such
as querying by rank. See the
[t-digest](https://redis.io/docs/latest/develop/data-types/probabilistic/t-digest)
reference for more information.

### Ranking

A [Top-K](https://redis.io/docs/latest/develop/data-types/probabilistic/top-k)
object estimates the rankings of different labeled items in a data
stream according to frequency. For example, you could use this to
track the top ten most frequently-accessed pages on a website, or the
top five most popular items sold.

The example below adds several different items to a Top-K object
that tracks the top three items (this is the second parameter to
the `topKReserve()` method). It also shows how to list the
top *k* items and query whether or not a given item is in the
list.

Foundational: Track top K most frequent items in a data stream with Top-K for efficient ranking without storing all items

**Difficulty:** Intermediate

**Available in:** Java (Asynchronous - Lettuce), Java (Reactive - Lettuce)

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> topkExample = asyncCommands
                    .topKReserve("top_3_songs", 3L,
                            TopKReserveArgs.Builder.width(2000L).depth(7L).decay(0.925))
                    .thenCompose(res31 -> {
                        System.out.println(res31);
                        // >>> OK
                        return asyncCommands.topKIncrBy("top_3_songs",
                                IncrementPair.of("Starfish Trooper", 3000L),
                                IncrementPair.of("Only one more time", 1850L),
                                IncrementPair.of("Rock me, Handel", 1325L),
                                IncrementPair.of("How will anyone know?", 3890L),
                                IncrementPair.of("Average lover", 4098L),
                                IncrementPair.of("Road to everywhere", 770L));
                    })
                    .thenCompose(res32 -> {
                        System.out.println(res32);
                        // >>> [null, null, null, Rock me, Handel, Only one more time, null]
                        return asyncCommands.topKList("top_3_songs");
                    })
                    .thenCompose(res33 -> {
                        System.out.println(res33);
                        // >>> [Average lover, How will anyone know?, Starfish Trooper]
                        return asyncCommands.topKQuery("top_3_songs", "Starfish Trooper", "Road to everywhere");
                    })
                    .thenAccept(res34 -> {
                        System.out.println(res34);
                        // >>> [true, false]
                    })
                    .toCompletableFuture();

            topkExample.join();
```

##### Java (Reactive - Lettuce)

```java
            String res31 = reactiveCommands.topKReserve("top_3_songs", 3L,
                    TopKReserveArgs.Builder.width(2000L).depth(7L).decay(0.925)).block();
            System.out.println(res31);
            // >>> OK

            List<Value<String>> res32 = reactiveCommands
                    .topKIncrBy("top_3_songs",
                            IncrementPair.of("Starfish Trooper", 3000L),
                            IncrementPair.of("Only one more time", 1850L),
                            IncrementPair.of("Rock me, Handel", 1325L),
                            IncrementPair.of("How will anyone know?", 3890L),
                            IncrementPair.of("Average lover", 4098L),
                            IncrementPair.of("Road to everywhere", 770L))
                    .collectList()
                    .block();
            System.out.println(res32);
            // >>> [Value.empty, Value.empty, Value.empty, Value[Rock me, Handel], Value[Only one more time], Value.empty]

            List<String> res33 = reactiveCommands.topKList("top_3_songs").collectList().block();
            System.out.println(res33);
            // >>> [Average lover, How will anyone know?, Starfish Trooper]

            List<Boolean> res34 = reactiveCommands
                    .topKQuery("top_3_songs", "Starfish Trooper", "Road to everywhere")
                    .collectList()
                    .block();
            System.out.println(res34);
            // >>> [true, false]
```



