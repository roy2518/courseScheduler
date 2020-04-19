import React, { Fragment } from 'react'
import { Segment, Button, List } from 'semantic-ui-react'
class ScheduleList extends React.Component {

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
                    <List.Item key={[course.subject, course.course_num, course.type, course.id]}>
                        {course.subject} {course.course_num} / {course.type} ({course.start_time}-{course.end_time} {days})
                        <Button floated='right' course={course} onClick={(e, { course }) => { this.props.removeCourse(course) }}>Remove</Button>
                    </List.Item>
                )
            })
        )
    }

    render() {
        return (
            <Fragment>
                <span style={{fontSize: 'x-large', fontWeight: 'bold', paddingBottom: '20px'}}>Current Courses</span>
                <Button floated='right' onClick={this.props.saveSchedule}>Save</Button>
                <List divided>
                    {this.renderCourses(this.props.courses)}
                </List>
            </Fragment>
        )
    }
}

export default ScheduleList