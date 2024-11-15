# Case Study

SUMMARY:
This simple program was created to monitor the state of a critical business application, and correct that status. This increased IT efficiancy, decreased client down-time, and provided rapid resolution.

THE NEED:
I had a client that would reach out to me often with an issue. All of their client side versions of their busniess application would suddendly not allow them to authenticate to the server. Upon investigation, it was determined that the licensing process for that software would close out intermittently. With poor software support from the vendor, and lackluster logging, a team member needed to log in and restart that process. With no fix being provided from the vendor, company downtime, and sheer inconvenience for team members, we needed to automate this process.
 
THE FIX:
A program was developed that detects every 5 minutes if the specific licensing process was still active, and if it was not, the monitor would trigger the process to start. Logging was included to verify the fix, and help analyze timing with the failing process. Added convenience was provided by enabling the monitor to launch during server startup.