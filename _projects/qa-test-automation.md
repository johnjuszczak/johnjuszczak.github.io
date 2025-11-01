---
title: "QA Test Automation"
summary: "Automation that mirrors QA's Zephyr plans across maps and publishes results to Jira Zephyr and Slack"
tags: [Unreal, Python, Jenkins, CI/CD, Jira, Zephyr, Slack, REST, Automation]
permalink: /projects/qa-test-automation/
image_path: /assets/images/uee253110.jpg
show_date: false
---

{% capture project_body %}
### Scope
<ul>
  <li>Automated the exact QA plans defined in Jira Zephyr with one-to-one mapping of manual cases to automated suites</li>
  <li>Executed coverage across required maps and bundled results from the Python runner</li>
  <li>Integrated with the Zephyr API to create and update Test Runs and Test Cycles with pass and fail outcomes</li>
  <li>Implemented persistent result storage and correlation to builds and suites</li>
  <li>Posted build and suite outcomes to Slack channels for rapid triage and coordination</li>
</ul>

### Tech
Unreal Engine, Python, Jenkins, Jira Zephyr API, Slack API, REST

### Results
<ul>
  <li>Direct alignment between QA specifications and automated execution</li>
  <li>Consistent, bundleable artifacts suitable for CI dashboards and audit</li>
  <li>Reduced manual verification effort through reliable map level coverage</li>
  <li>Faster triage via Slack notifications tied to builds and suites</li>
</ul>
{% endcapture %}

{% include project_split.html body=project_body %}
