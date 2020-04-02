import React, {Fragment} from 'react'
import {Grid, Segment} from 'semantic-ui-react'
import ClassSearch from './ClassSearch'
import Calendar from './Calendar'


class App extends React.Component {

    constructor(props) {
        super(props)
        this.addCourse = this.addCourse.bind(this)
    }

    state = {
        courses: []
    }

    addCourse = (course) => {

        let courses = [...this.state.courses]

        let courseEvent = {
            title: `${course.subject} ${course.course_num} / ${course.type}`,
            daysOfWeek: [],
            startTime: course.start_time,
            endTime: course.end_time,
            start: new Date()
        }

        if (course.days.mon === true) {
            courseEvent.daysOfWeek.push(1)
        }
        if (course.days.tues === true) {
            courseEvent.daysOfWeek.push(2)
        }
        if (course.days.wed === true) {
            courseEvent.daysOfWeek.push(3)
        }
        if (course.days.thur === true) {
            courseEvent.daysOfWeek.push(4)
        }
        if (course.days.fri === true) {
            courseEvent.daysOfWeek.push(5)
        }

        courses.push(courseEvent)
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