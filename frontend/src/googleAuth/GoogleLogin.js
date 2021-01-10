import axios from "axios";

const googleLogin = async (accessToken) => {
    let res = await axios.post(
      "http://localhost:8000/auth/google/",
      {
        access_token: accessToken,
      }
    );
    console.log(res);
    return res.status;
  };

export default googleLogin;