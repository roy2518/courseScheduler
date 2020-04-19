import React from 'react';
import {BrowserRouter, Route} from 'react-router-dom'
import App from './App'
import Login from './Login'

class Browser extends React.Component { 
  
    state = {
      netid: null
    }

    setNetID = (id) => {
        this.setState({netid: id});
    }

  render(){
    return (
      <BrowserRouter>
            <Route path="/" exact render={(props) => <App netid={this.state.netid}/>} />
            <Route path="/login" render={(props) => <Login setNetID={this.setNetID}/>} />
      </BrowserRouter>
    );
  }
}

export default Browser;