# IDETRA
IDETRA's educational, project management and blueprints platform

Live project (at https://idetra.org )

Dev notes:

- CI stands for "Center of Intelligence" and its the project management platform.

- I need to create the backend for all pages that starts with "ci" under "idetra/templates" (their front end are done).

- all notes of what needs to be created are located inside each "ci..." html page (at the top of the page)

- apart of CI dev, there are a couple of fixes needed:

1) the check ("v") before each lesson name when its quizz is succefully finished by the user is missing. This is visually located on the list of the lateral menu under EDU, inside a loop (the "v" is already placed on the frontend as an icon <i fa ...> </i>.)

2) when the user finishes the courses flagged as "executive" and "project manager", the boolean from his profile is not changing to True (visually this resides on the user's profile when the user opts in to help IDETRA on "edit profile" at the bottom of the page. This is necessary and is already coded in multiple instances on the platform, including CI)

- you might find the need to clean up or change some of the code.
