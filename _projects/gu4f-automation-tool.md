---
title: "GauntletU4F.AutomationTool"
summary: "Unreal Automation Tool extension for functional test orchestration on real devices"
tags: [Unreal, UAT, C#, Automation, Android, iOS, Networking, AWS, Linux, Windows]
permalink: /projects/gu4f-automation-tool/
image_path: /assets/images/uee253110.jpg
show_date: false
---

{% capture project_body %}
### Scope
<ul>
  <li>Coordinated packaged game launches on Android/iOS and instructed the GU4F test plugin which plans, suites, and steps to run</li>
  <li>Selected and enforced the correct map per test and synchronized start conditions across all clients</li>
  <li>Implemented the server role: initial Windows host, later Linux on an AWS agent, with per-test session lifecycle</li>
  <li>Managed client-server syncing, connection checks, and timeouts to recover from device or launch failures</li>
  <li>Evolved the protocol so more of the sync responsibilities could be handled inside the GU4F test plugin</li>
</ul>

### Tech
C#, Unreal Automation Tool (UAT), Android, iOS, Networking, AWS Linux, Windows

### Results
<ul>
  <li>Deterministic, repeatable functional test runs on real devices</li>
  <li>Lower flakiness through robust launch, connection, and timeout handling</li>
  <li>Scalable orchestration via cloud-hosted server sessions</li>
  <li>Clear separation of orchestration (UAT) from in-game test logic (GU4F plugin)</li>
</ul>
{% endcapture %}

{% include project_split.html body=project_body %}
