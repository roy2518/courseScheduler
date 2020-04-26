import React, { Fragment } from 'react'
import { Segment, Button, List, Divider } from 'semantic-ui-react'
import ValidationPopup from './ValidationPopup'

class CurrentCourses extends React.Component {

    renderCourses = (courses) => {

        return (
            courses.map((course) => {

                let days = ''
                if (course.days.mon === true) {
                    days = days.concat('M')
                }
                if (course.days.tues === true) {
                    days = days.concat('T')
                }
                if (course.days.wed === true) {
                    days = days.concat('W')
                }
                if (course.days.thur === true) {
                    days = days.concat('Th')
                }
                if (course.days.fri === true) {
                    days = days.concat('F')
                }

                return (
                    <List.Item style={{ fontSize: 'large' }} key={[course.subject, course.course_num, course.type, course.id]}>
                        {course.subject} {course.course_num} / {course.type} ({course.start_time}-{course.end_time} {days})
                        <Button floated='right' color='pink' course={course} onClick={(e, { course }) => { this.props.removeCourse(course) }}>Remove</Button>
                    </List.Item>
                )
            })
        )
    }

    render() {
        return (
            <Fragment>
                <span style={{ fontSize: 'x-large', fontWeight: 'bold', paddingBottom: '20px' }}>Current Courses</span>
                {this.props.scheduleID ? 
                    <span style={{ fontSize: 'large' }}>   (currently editing schedule #{this.props.scheduleID})</span> 
                    : <span style={{ fontSize: 'large' }}>   (currently editing new schedule)</span>}
                <Button floated='right' color='blue' onClick={this.props.saveSchedule}>Save</Button>
                <ValidationPopup courses={this.props.courses} trigger={<Button floated='right' color='orange' content='Validate'/>} />
                <Divider hidden/>
                <List divided>
                    {this.renderCourses(this.props.courses)}
                </List>
                {this.props.courses.length > 0 ? 
                    <Button floated='right' color='red' onClick={(e) => {this.props.removeAllCourses()}}>Remove All</Button>
                    : null}
            </Fragment>
        )
    }
}

export default CurrentCourses