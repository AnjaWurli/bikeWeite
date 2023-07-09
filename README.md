# bikeWeite

Welcome! This small app visualizes the region that you can reach within a
certain distance that you define. You can use it to enter an address and see
what you can reach by bike on an interactive map.

## How to run in development mode

To run it locally on your computer, you need to install npm and python
dependencies, build and deploy the frontend, do the migrations and run the
django development server. More specific instructions

1. install the npm dependencies via `npm install`
2. build the frontend via `npm run build`
3. install the python depencencies via
   ```bash
   pip install pipenv
   pipenv install
   ```
4. do the database migrations via `pipenv run manage migrate`
5. run the frontend development server via `npm run dev`
6. open another terminal and run the django server via `pipenv run manage runserver`
7. open the app at http://127.0.0.1:8000/
