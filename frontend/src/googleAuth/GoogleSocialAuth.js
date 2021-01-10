import React, { Component } from 'react';
import GoogleLogin from 'react-google-login';
import googleLogin from './GoogleLogin'

class GoogleSocialAuth extends Component {

  render() {
    return (
      <div className="App">
        <h1>LOGIN WITH GOOGLE</h1>

        <GoogleLogin
          clientId="351400190668-nj6qch3c235giuacshoe15vqfb0iol2a.apps.googleusercontent.com"
          buttonText="Login"
          onSuccess={(res) => {googleLogin(res.accessToken).then(r => console.log(r))}}
          onFailure={(res) => console.log(res)}
        />
      </div>
    );
  }
}

export default GoogleSocialAuth;