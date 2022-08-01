# COREELS Project Documentation {intro}

> A short movie streaming platform developed by Team 118 of Zuri/I4G Training Participants
> Movies are uploaded only by **Verified College** students but can be streamed by anyone from anywhere around the world as long as they're signed into their COREELS account.

## Installation {installation}

The project is built and deployed with **Django** and below are instructions on how to set it up and run it locally on your system.

1. **Clone a Copy of the Project.**
   Clone a copy of the project from GitHub or extract the zipped archive into a directory on your computer where you can easily access it.
2. **Download and Install Python 3**

   - Go to [Python](www.python.org/downloads/ "Download Python 3") and install it on your computer.
   - Open your terminal and type `python --version`. If you see output similar to `Python 3.10.4` then you have successfully installed python.
3. **Create a Virtual Environment**

   - Open a terminal and `cd` into the folder/directory where you cloned your copy of the COREELS project into.
   - Run `python -m venv venv` to create a virtual environment for your project.
   - Once your virtual environment has been created, run `venv/scripts/activate` (_Windows users_) OR `source venv/bin/activate` (_Linux/Unix-like users_).
   - If everything goes well, your terminal prompt will be prepended with `venv`.
4. **Install Required Packages**
   Now that python and virtual environemnt is set up;

   - Run `where.exe python` (_Windows users_) OR (_Linux/Unix-like users_) on your terminal. If everything works well so far, you should see output similar to below output on your terminal.

     ```bash
     C:\Festus\Codes\Organisations\Zuri\coreels\venv\Scripts\python.exe
     C:\Users\FESTUS\AppData\Local\Programs\Python\Python310\python.exe
     ```

     Where each of the output line is a path to executabe python file.
   - Now install required python packages by running: `pip install -r requirements.txt`.
   - This command will install all the required packages that have been listed in our requirements.txt file.

## How To Use {how-to}

Follow below steps to run the project and test how it works.

1. Ensure you're in same location as the file `manage.py` and that your virtual environemnt is still activated.
2. Type `python manage.py migrate`.
3. If everything works as it should, **django** will use migrations file in the project apps and create a new (**sqlite3**) database in the same location as **manage.py** file.
4. Create a superuser account by running: `python manage.py createsuperuser` command on the terminal. Provide desired **username**, **email address**, **password** and **password confirmation** as being prompted.
5. Next, run `python manage.py runserver`. This will start a development server on **localhost** on port **8000** which can be accessed via: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

That is all. You can now visit above address to see the content of the website and start playing around with the functionalities.

## Developers {developers}

This project was built, developed and deployed by Team 118 of Zuri/I4G training participants. The project idea was from Zuri.

## License {license}

The code is MIT licensed. To understand your rights, privileges and limitations better, please refer to the [LICENSE](LICENSE "License File").

## Thanks & Credits {credits}

We sincerely appreciate the organizers of this training (I4G/Zuri) and their partners for giving us the opportunity to participate and learn from the best teams, tutors and mentors all for free.
