---
title: "Mobile Device Performance Telemetry"
summary: "Unreal Engine performance telemetry system plugin for android and iOS devices"
tags: [Unreal, Performance, Telemetry, NewRelic, Automation, Firebase, Unreal Engine, Android, iOS, C#]
permalink: /projects/nonfunctional-testing/
image_path: /assets/images/uee253110.jpg
show_date: false
---

{% capture project_body %}
### Scope
<ul>
  <li>Extended a UE plugin to emit performance telemetry from real devices for map-scoped scenarios</li>
  <li>Integrated with Firebase dashboards, then migrated to New Relic for centralized reporting and analysis</li>
  <li>Defined telemetry keys and cycle-keys to correlate device metrics with scenarios and time slices</li>
  <li>Helped build and support a companion UE plugin to orchestrate perf runs: spawn/manage bots, drive cameras, capture screenshots alongside metrics, and sample device vitals</li>
  <li>Coordinated execution with UAT in C# and Python tooling to run against Android/iOS device racks</li>
</ul>

### Tech
Unreal Engine, UAT, C#, Python, Android, iOS, Firebase, New Relic

### Results
<ul>
  <li>Repeatable, map-scoped performance baselines across Android and iOS</li>
  <li>Correlated telemetry, screenshots, and scenario metadata for faster triage</li>
  <li>Dashboards that exposed regressions early and reduced manual perf checks</li>
  <li>Lower flakiness via orchestrated device runs and scenario synchronization</li>
</ul>
{% endcapture %}

{% include project_split.html body=project_body %}

