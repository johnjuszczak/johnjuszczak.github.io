---
title: "Test Bot Tool"
summary: "BehaviorTree based automated testing for UE "
tags: ["Unreal Engine", "Bots", "Automation", "C++", "Testing"]
permalink: /projects/test-bot-tool/
image_path: /assets/images/ueta253110.jpg
show_date: false
---

{% if page.summary %}
<p class="page__lead">{{ page.summary }}</p>
{% endif %}

### Description
BehaviorTree implemented bot behavior integrated with GauntletU4F functional testing tool that spawns and drives bots through deterministic behaviors to validate gameplay flows in a multiplayer context.

### Scope
<ul>
  <li>Extended the functional testing tool to support bot-driven tests using Behavior Trees and Blackboard data</li>
  <li>Introduced simplified scripting per net role with Server and N Client nodes exposed directly in Blueprint</li>
  <li>Added test assets for composing behaviors and validations, including health/attacker checks and control-point objectives</li>
  <li>Implemented per-bot Behavior Tree assignment within test plans, with automatic bot spawning and configuration</li>
  <li>Built client/bot identification and ID assignment so validations could target specific bots consistently</li>
  <li>Co-designed library of reusable “test behaviors” with the AI team and integrated execution into the existing test plan workflow</li>
</ul>

### Tech
Unreal Engine, C++, Blueprints, Behavior Tree, Blackboard, Automation

### Results
<ul>
  <li>Lowered effort to author multiplayer bot tests via per-role Blueprint nodes and per-bot Behavior Trees</li>
  <li>Deterministic validations that coupled bot behaviors with measurable outcomes</li>
  <li>Broader adoption by AI and gameplay developers due to reusable behavior and validation assets</li>
  <li>Consistent mapping between clients and bots enabling stable test orchestration</li>
</ul>
