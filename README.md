# bikeWeite

Welcome! This small app visualizes the region that you can reach within a
certain distance that you define. You can use it to enter an address and see
what you can reach by bike on an interactive map.

<img width="1202" alt="Bildschirmfoto 2023-07-24 um 11 23 27" src="https://github.com/AnjaWurli/bikeWeite/assets/118619305/fd716f0f-17c1-4976-8c5f-5891812cf675">
<img width="866" alt="Bildschirmfoto 2023-07-24 um 12 23 39" src="https://github.com/AnjaWurli/bikeWeite/assets/118619305/66279a38-0b4a-4808-99a1-3f7a95a2fb72">

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
