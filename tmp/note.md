================================================================
if (cacheHelperService.getClientSetting(Enums.ClientSetting.MoneySpace, false)) {
    addMenuItemHandler.addMenuItemEvent(
        R.id.fwb_hub_menu_item,
        R.drawable.ic_menu_fwb,
        activity.getString(R.string.fwb_hub_title),
        ShowFragmentModel(
            Enums.FragmentEnum.FwbGuidanceArticle,
            Bundle().apply {
                putString(Enums.BundleKeys.FwbGuidanceCategoryCode.name, "SavingUp")
                putString(Enums.BundleKeys.FwbGuidanceArticleCode.name, "understandinginvestment")
            }
        )
    )
}

================================================================
JAVA11 Android Release - QA: https://webapptfs.asbbank.co.nz/DefaultCollection/MobileApplications/_build/results?buildId=555029&view=results
# Mobile distribution site - ASBMobile/QA 
ASBMobile-22.03.0-555029-qa-release-universal.apk
Created: 1/03/2022 5:33:22 PM

JAVA11 Android Release - Dev: https://webapptfs.asbbank.co.nz/DefaultCollection/MobileApplications/_build/results?buildId=555039&view=results
# Mobile distribution site - ASBMobile/Dev
ASBMobile-22.03.0-22.04.2-555039-dev-release-universal.apk
Created: 1/03/2022 6:05:02 PM

================================================================

MissionControl > Features > Clustered Mojo Feature > Feature Versions > QA

Add "Digital.FwbGuidance.Experience" to "API Endpoints"

Click "Show Advanced Options".

Click "Add Exposed Interface", and add following entity:
    Interface name: LaunchSavingsGoal
    URL: native://asbmobile/savingsGoal

Click "Add Exposed Interface", and add following entity:
    Interface name: LaunchContactUs
    URL: native://asbmobile/contactUs

Scroll down to section "Associated Feature Entry Points"

Click "Add Invoked Interface", and add following entity:
    Target Feature: Clustered Mojo Feature
    Interface name: LaunchSavingsGoal

Click "Add Invoked Interface", and add following entity:
    Target Feature: Clustered Mojo Feature
    Interface name: LaunchContactUs

Save the change.

MissionControl > Containers > Mobile > Environments > Mobile Container QA - V2 > Api Endpoints

Click "+" button, and add following entity:
    Api Endpoint: Digital.FwbGuidance.Experience
    Isam Junction: QA ISAM OAuth DMZ Gateway

Save the change.

================================================================
https://webapptfs.asbbank.co.nz/DefaultCollection/MobileApplications/_git/ASBMobile.Android?path=%2FASBMobile%2Fsrc%2Fmain%2Fjava%2Fnz%2Fco%2Fasb%2Fmobile%2Ffeature%2Ffinancialwellbeinghub&version=GBrelease%2F22.03.0&_a=contents

ASBMobile/src/main/java/nz/co/asb/mobile/feature/financialwellbeinghub
  - /components/**guidance**
  - /guidance/**


================================================================
================================================================
================================================================
================================================================
================================================================
