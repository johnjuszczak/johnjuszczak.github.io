---
title: "GauntletU4F"
summary: "Unreal Engine Functional Testing Tool Plugin Utilizing Gauntlet"
tags: [Unreal, Gauntlet, Slate, Automation, Python, Android, iOS, UAT]
permalink: /projects/gauntletu4f/
image_path: /assets/images/ueta253110.jpg
show_date: false
---

{% if page.summary %}
<p class="page__lead">{{ page.summary }}</p>
{% endif %}

### Scope
<ul>
  <li>Slate frontend listing tests with categories, selection, and execution controls</li>
  <li>Blueprint-based test step asset defining scripted behaviors per step</li>
  <li>Blueprint-based test plan asset composing steps, naming plans and steps, optional setup and teardown</li>
  <li>Per-step configuration for map asset, auto-load behavior, and the GU4F test asset to execute</li>
  <li>Runs in editor and in packaged builds; spawns additional PIE viewports for multi-client scenarios</li>
  <li>Displays results after execution and exports results as CSV</li>
  <li>Integrated with GU4F.AutomationTool and later a Python orchestration tool to run on real devices</li>
</ul>

### Tech
Unreal Engine (C++/UObject, Slate, Blueprints), Gauntlet, UAT, Python, CSV

### Results
<ul>
  <li>Deterministic functional scenarios executable in editor and on Android/iOS devices</li>
  <li>Faster iteration via in-editor composition of plans and steps</li>
  <li>Consistent, exportable results for CI and device-lab runs</li>
  <li>Lower onboarding cost for writing and organizing functional tests</li>
</ul>

