# Google Workspace SAML integration guide

```json metadata
{
  "schema_version": 2,
  "title": "Google Workspace SAML integration guide",
  "description": "This integration guide shows how to configure Google Workspace as a SAML single sign on provider for your Redis Cloud account.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"create-the-google-workspace-saml-application","title":"Create the Google Workspace SAML application"}],"id":"step-1-set-up-your-identity-provider-idp","title":"Step 1: Set up your identity provider (IdP)"},{"children":[{"id":"sign-in-to-redis-cloud","title":"Sign in to Redis Cloud"},{"id":"activate-saml-in-access-management","title":"Activate SAML in Access Management"}],"id":"step-2-configure-saml-support-in-redis-cloud","title":"Step 2: Configure SAML support in Redis Cloud"},{"id":"step-3-add-a-custom-attribute-to-google-workspaces-user-profile","title":"Step 3: Add a custom attribute to Google Workspace's user profile"},{"id":"step-4-finish-saml-configuration-in-google-workspaces-redis-cloud-application","title":"Step 4: Finish SAML configuration in Google Workspace's Redis Cloud Application"},{"id":"step-5-activate-saml-integration","title":"Step 5: Activate SAML integration"}]}

,
  "codeExamples": []
}
```


This guide shows how to configure [Google Workspace](https://workspace.google.com/) as a SAML single sign-on identity provider (IdP) for your Redis Cloud account.

To learn more about Redis Cloud support for SAML, see [SAML single sign-on](https://redis.io/docs/latest/operate/rc/security/access-control/saml-sso).

Before completing this guide, you must [verify ownership of any domains](https://redis.io/docs/latest/operate/rc/security/access-control/saml-sso#verify-domain) you want to associate with your SAML setup.

## Step 1: Set up your identity provider (IdP)

### Create the Google Workspace SAML application

1. Sign in to your [Google Workspace admin account](https://admin.google.com/).

1. From the main menu, select **Apps** then **Web and mobile apps**.

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_0.png)

1. Once in Web and mobile apps, select **Add custom SAML app** from the dropdown list.

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_1.png)

1. To begin, change the **App name** and **Description** to **Redis Cloud**. You can also choose an **App icon** for the application. We suggest you upload a Redis icon. Once complete, select **Continue**.

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_2.png)

1. In the next screen, you will find all of the information needed to configure SAML in Redis Cloud. Select the **copy** button for the following information sections:

   * SSO URL
   * Entity ID
   * Certificate

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_3.png)

Once complete, select **Continue**.

## Step 2: Configure SAML support in Redis Cloud

Now that you have your Google Workspace IdP server information, configure support for SAML in Redis Cloud.

### Sign in to Redis Cloud

Sign in to your account on the [Redis Cloud console](https://cloud.redis.io/#/login).

### Activate SAML in Access Management

To activate SAML, you must have a local user (or social sign-on user) with the `owner` role. If you have the correct permissions, you will see the **Single Sign-On** tab.

1. Add the information you saved previously in the **Google identity provider details** screen. This includes:

    * **Issuer (IdP Entity ID)**: `Entity ID`.
    * **IdP server URL**: `SSO URL`.
    * **Assertion signing certificate**: `Certificate`.

   ![](https://redis.io/docs/latest/images/rc/saml/sm_saml_1.png)

   Select **Enable** and wait a few seconds for the status to change.

1. Select **Download** to get the service provider (SP) metadata. Save the file to your local hard disk.

   ![](https://redis.io/docs/latest/images/rc/saml/sm_saml_3.png)

1. Open the file in any text editor. Save the following text from the metadata:

    * **EntityID**: The unique name of the service provider (SP).

      ![](https://redis.io/docs/latest/images/rc/saml/sm_saml_4.png)

   * **Location**: The location of the assertion consumer service.

  ![](https://redis.io/docs/latest/images/rc/saml/sm_saml_5.png)

## Step 3: Add a custom attribute to Google Workspace's user profile

1. From the main menu in Google Workspace, select **Directory** then **Users**, and from the **more options** dropdown select **Manage custom attributes**.
   
   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_7.png)

1. From the **Manage user attributes** screen, select **Add Custom Attribute**.

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_8.png)

1. Add the following information for the new custom attribute:

   * **Category**: `Redis Cloud`
   * **Name**: `redisAccountMapping`
   * **Info type**: `Text`
   * **Visibility**: `Visible to user and admin`
   * **No. of values**: `Single`

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_9.png)

   Once complete, select **Add**. The summary page now displays the new **redisAccountMapping** custom field.

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_10.png)

1. From the main menu in Google Workspace, select **Directory** then **Users**, then select the user you wish to configure. 

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_11.png)

1. Each user who needs to access Redis Cloud through SAML needs to define the **redisAccountMapping** attribute. The `redisAccountMapping` key-value pair consists of the lowercase role name (owner, member, manager, billing_admin, or viewer) and your Redis Cloud Account ID found in the [account settings](https://redis.io/docs/latest/operate/rc/accounts/account-settings).

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_12.png)

   Once complete, select **Save**.

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_13.png)

   Repeat this step for each user who needs to define the `redisAccountMapping` attribute.

## Step 4: Finish SAML configuration in Google Workspace's Redis Cloud Application

1. Return to the **Service provider details** screen in Google Workspace, and add the following information:

   * **ACS URL**: The Location from the downloaded service provider (SP) metadata
   * **Entity Id**: The EntityID from the downloaded service provider (SP) metadata

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_6.png)

   Leave the **Name ID** default information as it is. Once complete, select **Continue**.

1. Configure the **Redis Cloud** application's attribute mappings. Select **Add Mapping**.

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_14.png)

   In the next screen, map these attributes:

   * **Primary Email**: `Email`
   * **First name**: `FirstName`
   * **Last name**: `LastName`
   * **redisAccountMapping**: `redisAccountMapping`

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_15.png)

   Once complete, select **Finish**.

1. Next, we need to turn on the Redis Cloud service for all users, select **Web and mobile apps** -> **Redis Cloud** and then **service status**. Select **ON for everyone**. Once complete, select **Save**.

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_16.png)

## Step 5: Activate SAML integration

The final step in our SAML integration with AWS IAM identity Center is to activate the SAML integration.

1. In the Single Sign-On screen, select **Activate**.

   ![](https://redis.io/docs/latest/images/rc/saml/sm_saml_8.png)

A logout notification screen displays, letting you know that you are redirected to Google's login screen.

1. Select the Google account you wish to login with.

   ![](https://redis.io/docs/latest/images/rc/saml/google_workspace_saml_18.png)

If everything is configured correctly, you will see the the Redis Cloud console screen. Your local account is now considered a SAML account. 

To log in to the Redis Cloud console from now on, click on **Sign in with SSO**.

![Sign in with SSO button](https://redis.io/docs/latest/images/rc/button-sign-in-sso.png)

