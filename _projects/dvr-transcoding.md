---
title: "DVR Transcoding"
summary: "Stream and download DVR recordings from your set-top box to the mobile app"
tags: [C++, Android, GoogleTest, Node.js]
permalink: /projects/dvr-transcoding/
image_path: /assets/images/dtvhr231025.jpg
show_date: false
---

{% capture project_body %}
### Scope
<ul>
  <li>Implemented on-box C++ server exposing recordings and using hardware transcoders to generate mobile-ready streams</li>
  <li>Built the client module within the DirecTV mobile app to browse recordings, stream, or download for offline use</li>
  <li>Designed adaptive bitrate logic that adjusted resolution/bitrate based on network conditions</li>
  <li>Created automated end-to-end tests with Node.js promise-based flows for client-server validation</li>
  <li>Practiced kanban sprints with up-front UML design reviews and iterative demos</li>
</ul>

### Tech
C++ (server and client components), SQLite, GoogleTest, Android (Java), Node.js (promise-based E2E)

### Results
<ul>
  <li>Reliable streaming and downloads from personal DVRs to mobile devices</li>
  <li>Maintainable client-server architecture with strong automated test coverage</li>
  <li>Smooth iterative delivery enabled by design-first sprints</li>
</ul>
{% endcapture %}

{% include project_split.html body=project_body %}
