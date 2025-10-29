---
layout: archive
title: "Projects"
permalink: /projects/
---

{% assign items = site.projects | sort: "title" %}
{% for p in items %}
- [{{ p.title }}]({{ p.url }}) — {{ p.summary }}
{% endfor %}
