---
title: "Backtrace Crash Reporting"
summary: "Cross-platform Unreal Engine crash reporting for Android and iOS"
tags: ["Unreal Engine", "C++", "Android", "Java", "NDK", "iOS", "Objective-C", "Swift", "Backtrace"]
permalink: /projects/backtrace-crash/
image_path: /assets/images/uts212302.jpg
show_date: false
---

{% capture project_body %}
### Scope
<ul>
  <li>Integrated Backtrace crash reporting into a single Unreal Engine project targeting Android and iOS</li>
  <li>Android: injected Java layer into the UE Android build and bridged native data via NDK</li>
  <li>iOS: implemented Objective-C and Swift crash-reporting keys and backend integration</li>
  <li>Unified report structure across platforms to keep metadata consistent</li>
</ul>

### Tech
Unreal Engine (C++), Android (Java, NDK), iOS (Objective-C, Swift), Backtrace SDK

### Results
<ul>
  <li>Consistent, cross-platform crash payloads with platform-specific metadata</li>
  <li>Single integration path maintained within the UE codebase for both mobile targets</li>
  <li>Reliable delivery of crash reports to the Backtrace backend from Android and iOS builds</li>
</ul>
{% endcapture %}

{% include project_split.html body=project_body %}
