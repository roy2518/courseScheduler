import React, { Fragment } from 'react'
import { Redirect } from 'react-router-dom'
import { Grid, Segment, Tab, Button } from 'semantic-ui-react'
import ClassSearch from './ClassSearch'
import Calendar from './Calendar'
import CurrentCourses from './CurrentCourses'
import ScheduleList from './ScheduleList'
import { client } from '../constants/api'


class App extends React.Component {

    constructor(props) {
        super(props)
        this.addCourse = this.addCourse.bind(this)
    }

    state = {
        courses: [],
        scheduleID: null
    }

    addCourse = (course) => {
        let courses = this.state.courses
        courses.push(course)
        this.setState({ courses: courses })
    }

    removeCourse = (course) => {
        let courses = this.state.courses
        const index = courses.indexOf(course);

        if (index > -1) {
            courses.splice(index, 1);
        }

        this.setState({ courses: courses })
    }

    saveSchedule = async () => {
        if (this.state.courses.length === 0) {
            alert('Please add some courses first!')
            return
        }
        let response
        if (this.state.scheduleID === null) {
            response = await client.post(`/schedule/${this.props.netid}`, { courses: this.state.courses })
            if (response.status % 200 > 100) {
                throw ('error')
            }
            this.setState({ scheduleID: response.data.sched_num })
        } else {
            response = await client.put(`/schedule/${this.props.netid}/${this.state.scheduleID}`, { courses: this.state.courses })
            if (response.status % 200 > 100) {
                throw ('error')
            }
        }

        console.log(response.data)
    }

    loadSchedule = (schedule) => {
        this.setState({ courses: schedule.courses, scheduleID: schedule.sched_num })
    }

    render() {

        if (this.props.netid === null) {
            return <Redirect push to="/login" />
        }

        return (
            <Fragment>
                <div style={{ position: "relative", boxShadow: "0 3px 4px -6px gray" }}>
                    <Grid columns={2}>
                        <Grid.Column width={8}>
                            <Segment basic padded>
                                <Calendar courses={this.state.courses} />
                            </Segment>
                            <CurrentCourses courses={this.state.courses} removeCourse={this.removeCourse} scheduleID={this.state.scheduleID} saveSchedule={this.saveSchedule} />
                        </Grid.Column>
                        <Grid.Column width={5} style={{ minWidth: "340px" }}>
                            <h1>Welcome, {this.props.netid}</h1>
                            <Tab panes={[
                                {
                                    menuItem: 'Search for Courses',
                                    render: () => <Tab.Pane><ClassSearch addCourse={this.addCourse} /></Tab.Pane>
                                },
                                {
                                    menuItem: 'Load Schedules',
                                    render: () => <Tab.Pane><ScheduleList netid={this.props.netid} loadSchedule={this.loadSchedule} /></Tab.Pane>
                                },
                                {
                                    menuItem: 'Create New Schedule',
                                    render: () => <Tab.Pane><Button fluid content={'Do It'} onClick={(e)=>{this.setState({courses: [], scheduleID: null})}}/></Tab.Pane>
                                }
                            ]} />
                        </Grid.Column>
                    </Grid>
                </div>
            </Fragment>
        )
    }
}

export default App