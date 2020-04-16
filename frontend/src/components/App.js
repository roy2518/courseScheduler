import React, {Fragment} from 'react'
import {Grid, Segment} from 'semantic-ui-react'
import ClassSearch from './ClassSearch'
import Calendar from './Calendar'
import ScheduleList from './ScheduleList'


class App extends React.Component {

    constructor(props) {
        super(props)
        this.addCourse = this.addCourse.bind(this)
    }

    state = {
        courses: []
    }

    addCourse = (course) => {
        let courses = this.state.courses
        courses.push(course)
        this.setState({courses: courses})
    }

    removeCourse = (course) => {
        let courses = this.state.courses
        const index = courses.indexOf(course);

        if (index > -1) {
            courses.splice(index, 1);
        }

        this.setState({courses: courses})
    }

    render() {
        return (
            <Fragment>
                <div style={{position: "relative", boxShadow: "0 3px 4px -6px gray"}}>
                    <Grid columns={2}>
                        <Grid.Column width={8}>
                            <Segment basic padded>
                                <Calendar courses={this.state.courses}/>
                            </Segment>
                            <h3>Current Courses</h3>
                            <ScheduleList courses={this.state.courses} removeCourse={this.removeCourse}/>
                        </Grid.Column>
                        <Grid.Column width={5} style={{minWidth: "340px"}}>
                            <ClassSearch addCourse={this.addCourse}/>
                        </Grid.Column>
                    </Grid>
                </div>
            </Fragment>
        )
    }
}

export default App