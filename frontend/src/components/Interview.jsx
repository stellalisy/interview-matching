import React from "react";
import axios from 'axios'
import {
  Login,
  Signup,
  TopHeader,
  Interviewee,
  Interviewer,
  Admin,
  UserInfo,
  Success,
  IntervieweeSchedule,
  InterviewerSchedule,
  AdminSchedule
} from './interview/index'
import '../css/styles.css'
import '../css/normalize.css'

class Interview extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: null, // user's role: Interviewee | Interviewer | Admin
      success: false,
      checkSchedule: false,
      info: {},
    };

    this.setUser = this.setUser.bind(this);
    this.signout = this.signout.bind(this);
    this.onSuccess = this.onSuccess.bind(this);
    this.onBack = this.onBack.bind(this);
  }

  setUser(user) {
    this.setState({ user })
  }

  login = async (user, checkSchedule = false) => {
    if (user.role === 'Admin' && checkSchedule) {
      var { data: data } = await axios.get('/api/get-interviewee')
      this.setState({ user, info: data, checkSchedule })
    } else {
      var { data: data } = await axios.get('/api/get-time')
      this.setState({ user, info: data, checkSchedule })
    }
  }

  scheduleSignout = async () => {
    try {
      await axios.get('/api/user/signout-schedule')
      this.setState({ user: null, success: false, checkSchedule: false })
    } catch (err) {
      console.log(err)
    }
  }

  signout = async () => {
    try {
      await axios.get('/api/user/signout')
      this.setState({ user: null, success: false })
    } catch (err) {
      console.log(err)
    }
  }

  onSuccess() {
    this.setState({ success: true })
  }

  onBack() {
    this.setState({ success: false })
  }

  render() {
    var { user, success, checkSchedule, info } = this.state
    var role = user && user.role
    var res = { ...user, ...info }

    return (
      <div>
        <TopHeader role={role} />

        <div className="card-wrapper">
          {
            user ?
              (checkSchedule ?
                (role === 'Interviewee' ? <IntervieweeSchedule {...res} callback={this.scheduleSignout} />
                  : role === 'Interviewer' ? <InterviewerSchedule {...res} callback={this.scheduleSignout} />
                    : role === 'Admin' ? <AdminSchedule {...res} callback={this.scheduleSignout} /> : ''
                ) :
                (success ? <Success callback={this.signout} back={this.onBack} /> :
                  <>
                    <UserInfo  {...user} callback={this.signout} />
                    {(role === 'Interviewee' ? <Interviewee {...this.state.info} callback={this.onSuccess} />
                      : role === 'Interviewer' ? <Interviewer  {...this.state.info} callback={this.onSuccess} />
                        : role === 'Admin' ? <Admin callback={this.onSuccess} /> : ''
                    )}
                  </>
                ))
              :
              <>
                <Signup callback={this.setUser} />
                <Login callback={this.login} />
              </>
          }
        </div>
      </div>
    )
  };
}

export default Interview