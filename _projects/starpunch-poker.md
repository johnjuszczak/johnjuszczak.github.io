---
title: "Starpunch Poker"
summary: "Cross-platform Texas Hold’em Application"
tags: ["C++", "Qt", "SQLite", "CQRS", "Event Bus", "Unit Testing", "GitHub Actions"]
permalink: /projects/starpunch-poker/
image_path: /assets/images/po2021324.jpg
show_date: false
---

{% if page.summary %}
<p class="page__lead">{{ page.summary }}</p>
{% endif %}

### Scope
<ul>
  <li>Domain-first poker engine implementing deterministic Texas Hold’em rules and hand evaluation</li>
  <li>Architected and designed CQRS style layer with Domain Driven Design approach</li>
  <li>Reusable adapters for both headless simulation and a Qt desktop UI</li>
  <li>CI implemented leveraging Github Actions workflows</li>
  <li>Designed and built persistence infrastructure using SQLite</li>
  <li>Achieved and maintained ~95% test coverage using GoogleTest automation</li>
</ul>

### Tech
C++, Qt, GoogleTest, GitHub Actions CI, CMake

### Results
<ul>
  <li>Reusable core engine decoupled from frameworks and UI</li>
  <li>Deterministic sims enabling regression tests and scenario analysis</li>
  <li>High test coverage with fast CI feedback</li>
  <li>Clean adapters enabling straightforward Qt integration and headless runs</li>
</ul>
