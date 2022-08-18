# EO (Austoni Alessandro 10524152)
This is a repository for Polimi Earth Observation exam/project.
The repo is created to perform change detection by C2VA given two images of the same area from two different time instants. A first step of coregistration is needed for a more accurate alignment of the two acquisitions and thus less errors in the change detection step. Indeed, the repository is composed of two main scripts: “Coregistration.ipynb” and “CD.ipynb”.
For a correct functioning of the code, please make sure to create a folder called “DATABASE” outside the main folder where this repository is locally stored. Make sure to have stored also the Gefolki repository that you can download here, located to the same path of the “DATABASE” folder.
The Gefolki package is necessary to run the coregistration script.
The database folder is used to store the raw satellite acquisitions that are used in the analysis (and will be lately accessed in the script through the database path). The coregistration script will also automatically generate some intermediate outputs during coregistration that will be lately used in the Change Detection script.
