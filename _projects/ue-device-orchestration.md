---
title: "Unreal Engine Device Orchestration Tool"
summary: "Python-based runner that builds, deploys, and executes UE test suites across Android and iOS device pools with server coordination"
tags: [Unreal, Python, Jenkins, CI/CD, Android, iOS, Linux, Windows]
permalink: /projects/ue-device-orchestration/
image_path: /assets/images/zep.jpg
show_date: false
---

{% if page.summary %}
<p class="page__lead">{{ page.summary }}</p>
{% endif %}

### Scope
<ul>
  <li>Replaced UAT-based orchestration with a Python application integrated directly with the studio Python build system</li>
  <li>Registered and managed device pools with selection by explicit devices or performance tiers low mid high</li>
  <li>Produced platform-correct builds based on selected devices and server target then installed to each device</li>
  <li>Stood up dedicated servers on Windows or Linux and coordinated client launches and connections</li>
  <li>Executed test suites across sets of maps with tests authored to be map agnostic</li>
  <li>Coordinated with the Test Bot Tool to drive Behavior Tree scenarios and validations on real devices</li>
  <li>Collected artifacts and results then bundled reports for local ad hoc runs and CI usage</li>
</ul>

### Tech
Unreal Engine, Python, Jenkins, CI/CD, Android, iOS, Linux, Windows

### Results
<ul>
  <li>Unified build deploy run loop for Android and iOS device racks</li>
  <li>Scalable orchestration that reduced flakiness by decoupling sync logic into engine side tools</li>
  <li>Map set execution enabled broader coverage with fewer bespoke tests</li>
  <li>Actionable bundled reports surfaced in Jenkins with consistent pass fail signals</li>
</ul>
