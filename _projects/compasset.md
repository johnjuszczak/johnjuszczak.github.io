---
title: "CompAsset"
summary: "Unreal Engine Asset Verification Automation Plugin"
tags: [Unreal, Slate, CI/CD, Jenkins, Perforce]
permalink: /projects/compasset/
image_path: /assets/images/ueta253110.jpg
show_date: false
---

{% if page.summary %}
<p class="page__lead">{{ page.summary }}</p>
{% endif %}

### Scope
<ul>
  <li>Implemented verification engine subsystem leveraging AssetRegistry.</li>
  <li>Cut verification time on large depots with 50K+ assets from >30mins to under 2mins.</li>
  <li>Provided Perforce integration for automated checked-out asset verification</li>
  <li>Designed and created frontend UI for verification configuration and execution using Slate</li>
  <li>Integrated test results directly to Jenkins CI/CD pipeline asset verification step, with asset test diffs across runs.</li>
</ul>

### Tech
C++ (Unreal/Slate), Jenkins, Perforce

### Results
<ul>
  <li>Exceptional runtime reduction and clearer diagnostics for asset issues.</li>
  <li>Improved CI/CD pipeline execution time.</li>
  <li>Increased tool adoption among artists.</li>
</ul>
