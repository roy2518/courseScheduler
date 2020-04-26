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
        if (courses.filter((otherCourse) => {
            return (otherCourse.subject === course.subject &&
                otherCourse.course_num === course.course_num &&
                otherCourse.type === course.type &&
                otherCourse.id === course.id
            )
        }).length > 0) {
            alert('Cannot add the same course twice!')
            return
        }
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

    removeAllCourses = () => {
        this.setState({ courses: [] })
    }

    createSchedule = () => {
        if (window.confirm('Are you sure you want to create a new schedule? Any unsaved work will be lost!')) {
            this.setState({ courses: [], scheduleID: null })
        }

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

        alert('Save successful!')
    }

    loadSchedule = (schedule) => {
        //if (schedule.sched_num === this.state.scheduleID) {
        //    alert('This schedule is already loaded!')
        //    return
        //}
        if (window.confirm('Are you sure you want to load this schedule? Any unsaved work will be lost!')) {
            this.setState({ courses: schedule.courses, scheduleID: schedule.sched_num })
        }
    }

    deleteSchedule = async (schedule) => {
        if (schedule.sched_num === this.state.scheduleID) {
            alert('You cannot delete a schedule while you are editing it!')
            return false
        }
        if (window.confirm('Are you sure you want to delete this schedule?')) {
            let response = await client.delete(`/schedule/${this.props.netid}/${schedule.sched_num}`)
            if (response.status % 200 > 100) {
                throw ('error')
            }
            alert('Deleted!')
            return true
        }

        return false
    }

    render() {

        if (this.props.netid === null) {
            return <Redirect push to="/login" />
        }

        return (
            <Fragment>
                <div style={{ position: "relative", boxShadow: "0 3px 4px -6px gray" }}>
                    <Grid columns={2} style={{ paddingLeft: '45px' }}>
                        <Grid.Column width={5} style={{ minWidth: '499px', paddingTop: '30px' }}>
                            <h1>Welcome, {this.props.netid}</h1>
                            <Tab panes={[
                                {
                                    menuItem: 'Search for Courses',
                                    render: () => <Tab.Pane><ClassSearch addCourse={this.addCourse} /></Tab.Pane>
                                },
                                {
                                    menuItem: 'Load Schedules',
                                    render: () => <Tab.Pane><ScheduleList netid={this.props.netid} loadSchedule={this.loadSchedule} deleteSchedule={this.deleteSchedule} /></Tab.Pane>
                                },
                                {
                                    menuItem: 'Create New Schedule',
                                    render: () => <Tab.Pane><Button fluid color='green' content={'Do It'} onClick={(e) => { this.createSchedule() }} /></Tab.Pane>
                                }
                            ]} />
                        </Grid.Column>
                        <Grid.Column width={9}>
                            <Segment basic>
                                <Calendar courses={this.state.courses} />
                            </Segment>
                            <CurrentCourses
                                courses={this.state.courses}
                                scheduleID={this.state.scheduleID}
                                removeCourse={this.removeCourse}
                                removeAllCourses={this.removeAllCourses}
                                saveSchedule={this.saveSchedule}
                            />
                        </Grid.Column>
                    </Grid>
                </div>
            </Fragment>
        )
    }
}

export default App