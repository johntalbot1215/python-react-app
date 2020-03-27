import React from 'react';
import Login from './Components/Login';
import './App.css';
import MainPage from './Components/MainPage';
import NewAccount from './Components/NewAccount';

import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom';

class App extends React.Component {
  render(){
    return ( 
      <Router>
        <Switch>
          <Route path="/new-account">
            <NewAccount />
          </Route>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/">
            <MainPage />
          </Route>
        </Switch>
      </Router>
    )
  }
}

export default App;
