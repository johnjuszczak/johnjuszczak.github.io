---
title: "Lime State Machine"
summary: "Header-only modern C++23 FSM library with a pragmatic runtime API and coroutine adapter"
tags: [C++23, Coroutines, CMake, GoogleTest, Header-only, C++]
permalink: /projects/lime-state-machine/
image_path: /assets/images/limsm.jpg
show_date: false
---

{% capture project_body %}
### Scope
<ul>
  <li>Event-driven runtime API for defining states, transitions, and effects</li>
  <li>Pluggable callable and effect policies for flexible output and side-effect handling</li>
  <li>Coroutine adapter for composing async workflows with awaitable transitions</li>
  <li>Small, dependency-free surface designed for embedding in tools and gameplay code</li>
  <li>Unit tests and minimal examples to validate transition logic and policies</li>
</ul>

### Tech
C++23, Coroutines, CMake, GoogleTest, Header-only

### Results
<ul>
  <li>Compact, zero-dependency FSM usable in production codebases</li>
  <li>Deterministic, testable transition logic with clear separation of concerns</li>
  <li>Easy integration into existing build systems and CI</li>
</ul>
{% endcapture %}

{% include project_split.html body=project_body %}
