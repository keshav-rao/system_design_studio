# Probabilistic data types

```json metadata
{
  "schema_version": 2,
  "title": "Probabilistic data types",
  "description": "Learn how to use approximate calculations with Redis.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"children":[{"id":"set-membership","title":"Set membership"},{"id":"set-cardinality","title":"Set cardinality"}],"id":"set-operations","title":"Set operations"},{"children":[{"id":"frequency","title":"Frequency"},{"id":"quantiles","title":"Quantiles"},{"id":"ranking","title":"Ranking"}],"id":"statistics","title":"Statistics"}]}

,
  "codeExamples": [{"codetabsId":"home_prob_dts-stepbloom","description":"Foundational: Use Bloom filters for memory-efficient set membership testing with false positive possibility","difficulty":"beginner","id":"bloom","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_prob_dts-stepbloom"}]},{"codetabsId":"home_prob_dts-stepcuckoo","description":"Foundational: Use Cuckoo filters for set membership testing with deletion support and faster lookups than Bloom filters","difficulty":"beginner","id":"cuckoo","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_prob_dts-stepcuckoo"}]},{"codetabsId":"home_prob_dts-stephyperloglog","description":"Foundational: Estimate set cardinality with HyperLogLog for memory-efficient counting of distinct items","difficulty":"beginner","id":"hyperloglog","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_prob_dts-stephyperloglog"}]},{"codetabsId":"home_prob_dts-stepcms","description":"Foundational: Track approximate item frequencies with Count-min sketch for memory-efficient statistics on data streams","difficulty":"intermediate","id":"cms","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_prob_dts-stepcms"}]},{"codetabsId":"home_prob_dts-steptdigest","description":"Foundational: Estimate quantiles and percentiles with t-digest for memory-efficient statistical analysis of large datasets","difficulty":"intermediate","id":"tdigest","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_prob_dts-steptdigest"}]},{"codetabsId":"home_prob_dts-steptopk","description":"Foundational: Track top K most frequent items in a data stream with Top-K for efficient ranking without storing all items","difficulty":"intermediate","id":"topk","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_home_prob_dts-steptopk"}]}]
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

```php
$r->sadd('ip_tracker', $newIpAddress);
```

The set can only contain each key once, so if the same address
appears again during the day, the new instance will not change
the set. At the end of the day, you could get the exact number of
distinct addresses using the `scard()` method:

```php
$numDistinctIps = $r->scard('ip_tracker');
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

**Available in:** PHP

##### PHP

```php
$r->del('recorded_users');
$r->bfreserve('recorded_users', 0.01, 1000);

$added = $r->bfmadd('recorded_users', 'andy', 'cameron', 'david', 'michelle');
echo json_encode($added), PHP_EOL;
// >>> [1,1,1,1]

$known = $r->bfexists('recorded_users', 'cameron');
echo $known, PHP_EOL;
// >>> 1

$unknown = $r->bfexists('recorded_users', 'kaitlyn');
echo $unknown, PHP_EOL;
// >>> 0
```



A Cuckoo filter has similar features to a Bloom filter, but also supports
a deletion operation to remove hashes from a set, as shown in the example
below.

Foundational: Use Cuckoo filters for set membership testing with deletion support and faster lookups than Bloom filters

**Difficulty:** Beginner

**Available in:** PHP

##### PHP

```php
$r->del('other_users');
$r->cfreserve('other_users', 1000);

$r->cfadd('other_users', 'paolo');
$r->cfadd('other_users', 'kaitlyn');
$r->cfadd('other_users', 'rachel');

$beforeDelete = [
    $r->cfexists('other_users', 'paolo'),
    $r->cfexists('other_users', 'kaitlyn'),
    $r->cfexists('other_users', 'rachel'),
    $r->cfexists('other_users', 'andy'),
];
echo json_encode($beforeDelete), PHP_EOL;
// >>> [1,1,1,0]

$r->cfdel('other_users', 'paolo');
$afterDelete = $r->cfexists('other_users', 'paolo');
echo $afterDelete, PHP_EOL;
// >>> 0
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

**Available in:** PHP

##### PHP

```php
$r->del('group:1', 'group:2', 'both_groups');

$r->pfadd('group:1', ['andy', 'cameron', 'david']);
$group1 = $r->pfcount('group:1');
echo $group1, PHP_EOL;
// >>> 3

$r->pfadd('group:2', ['kaitlyn', 'michelle', 'paolo', 'rachel']);
$group2 = $r->pfcount('group:2');
echo $group2, PHP_EOL;
// >>> 4

$r->pfmerge('both_groups', 'group:1', 'group:2');
$bothGroups = $r->pfcount('both_groups');
echo $bothGroups, PHP_EOL;
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

**Available in:** PHP

##### PHP

```php
$r->del('items_sold');
$r->cmsinitbyprob('items_sold', 0.01, 0.005);

$firstCounts = $r->cmsincrby(
    'items_sold',
    'bread', 300,
    'tea', 200,
    'coffee', 200,
    'beer', 100
);
echo json_encode($firstCounts), PHP_EOL;
// >>> [300,200,200,100]

$secondCounts = $r->cmsincrby(
    'items_sold',
    'bread', 100,
    'coffee', 150
);
echo json_encode($secondCounts), PHP_EOL;
// >>> [400,350]

$queriedCounts = $r->cmsquery('items_sold', 'bread', 'tea', 'coffee', 'beer');
echo json_encode($queriedCounts), PHP_EOL;
// >>> [400,200,350,100]
```



The advantage of using a CMS over keeping an exact count with a
[sorted set](https://redis.io/docs/latest/develop/data-types/sorted-sets)
is that a CMS has very low and fixed memory usage, even for
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

**Available in:** PHP

##### PHP

```php
$r->del('male_heights', 'female_heights', 'all_heights');

$r->tdigestcreate('male_heights');
$r->tdigestadd('male_heights', 175.5, 181, 160.8, 152, 177, 196, 164);

$maleMin = $r->tdigestmin('male_heights');
echo $maleMin, PHP_EOL;
// >>> 152

$maleMax = $r->tdigestmax('male_heights');
echo $maleMax, PHP_EOL;
// >>> 196

$maleQuantile = $r->tdigestquantile('male_heights', 0.75);
echo json_encode($maleQuantile), PHP_EOL;
// >>> ["181"]

$maleCdf = $r->tdigestcdf('male_heights', 181);
echo json_encode($maleCdf), PHP_EOL;
// >>> ["0.7857142857142857"]

$r->tdigestcreate('female_heights');
$r->tdigestadd('female_heights', 155.5, 161, 168.5, 170, 157.5, 163, 171);

$femaleQuantile = $r->tdigestquantile('female_heights', 0.75);
echo json_encode($femaleQuantile), PHP_EOL;
// >>> ["170"]

$r->tdigestmerge('all_heights', ['male_heights', 'female_heights']);
$allQuantile = $r->tdigestquantile('all_heights', 0.75);
echo json_encode($allQuantile), PHP_EOL;
// >>> ["175.5"]
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
the `topkreserve()` method). It also shows how to list the
top *k* items and query whether or not a given item is in the
list.

Foundational: Track top K most frequent items in a data stream with Top-K for efficient ranking without storing all items

**Difficulty:** Intermediate

**Available in:** PHP

##### PHP

```php
$r->del('top_3_songs');
$r->topkreserve('top_3_songs', 3, 7, 8, 0.9);

$evicted = $r->topkadd(
    'top_3_songs',
    'Starfish Trooper',
    'Only one more time',
    'Rock me, Handel',
    'How will anyone know?',
    'Average lover',
    'Road to everywhere'
);
echo json_encode($evicted), PHP_EOL;
// >>> [null,null,null,"Rock me, Handel","Only one more time",null]

$leaders = $r->topklist('top_3_songs');
echo json_encode($leaders), PHP_EOL;
// >>> ["Average lover","How will anyone know?","Starfish Trooper"]

$membership = $r->topkquery('top_3_songs', 'Starfish Trooper', 'Road to everywhere');
echo json_encode($membership), PHP_EOL;
// >>> [1,0]
```



