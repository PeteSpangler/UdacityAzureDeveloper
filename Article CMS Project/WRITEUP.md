# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

APP SERVICE:
The costs, scalability, and availability for a CMS app deployed through an App Service are reasonable. This is a fairly lightweight app,
so it does not need a significant compute capability. So even though the service plans are constant and the user is paying even when
no one is accessing the service, the reduced compute requirements of a CMS app are not expensive. Continous deployment through
GitHub workflows on the Azure portal makes updating the CMS app a snap.

VM:
The costs, scalability, and availability for a CMS app deployed through a VM are also reasonable. The VM allows for more customization
of the app's capability. It also would really benefit developers who have already built a CMS app but it might not be supported
through App Service but could work through the VM workflow. It also allows for more fine-tuning, so the developer can customize
the VM to optimize their CMS app.

My Choice:
I chose App Service because the CMS app is lightweight, does not require robust compute power, and is easy to deploy through Azure. The CMS
App is straightforward and runs on a Python codebase, which is supported by App Service. Overall, a simple choice.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

APP Service:
If the CMS app needed to be updated to allow for more compute capability, maybe playing movies or editing images or integrating
jupyter notebooks or something that would require more hardware, the costs could rise quickly. Also if there was functionality
desired that is not supported by Azure, that would be a roadblock for sure. Being unable to control the underlying software on the
server could also cause significant issues that could break your app.

VM:
If this CMS became more popular, it could become more expensive due to requiring more hardware/compute power. A new developer
coming onboard needs to know how the VM has been customized, so the on-boarding for new devs would take a bit longer. Also,
if the CMS needed more compute capability, it could also become significantly more expensive.