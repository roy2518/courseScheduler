import React from 'react'
import { Table, Button, Modal } from 'semantic-ui-react'

class CourseGroup extends React.Component {

    renderOfferings = (offerings) => {
        return offerings.map((offering) => {

            let days = ''
            if (offering.days.mon === true) {
                days = days.concat('M')
            }
            if (offering.days.tues === true) {
                days = days.concat('T')
            }
            if (offering.days.wed === true) {
                days = days.concat('W')
            }
            if (offering.days.thur === true) {
                days = days.concat('Th')
            }
            if (offering.days.fri === true) {
                days = days.concat('F')
            }

            return (
                <Table.Row>
                    <Table.Cell>{offering.subject} {offering.course_num} ({offering.type.toUpperCase()})</Table.Cell>
                    <Table.Cell>{offering.description}</Table.Cell>
                    <Table.Cell>{offering.class_rating}</Table.Cell>
                    <Table.Cell>{offering.start_time}-{offering.end_time}</Table.Cell>
                    <Table.Cell>{days}</Table.Cell>
                    <Table.Cell>{offering.professor}</Table.Cell>
                    <Table.Cell>{offering.prof_rating}</Table.Cell>
                    <Table.Cell>{Object.entries(offering.attributes).map(attr => {if (attr[1]) {return `${attr[0].toUpperCase()} `}})}</Table.Cell>
                    <Table.Cell>
                        <Button floated='right'
                            offering={offering}
                            onClick={(e, { offering }) => { this.props.addCourse(offering) }}
                        >
                            Add
                        </Button>
                    </Table.Cell>
                </Table.Row>
            )
        })
    }

    render() {
        return (
            <Modal trigger={this.props.trigger}>
                <Modal.Header>{this.props.courseName}</Modal.Header>
                <Modal.Content>
                    <Table>
                        <Table.Header>
                            <Table.Row>
                                <Table.Cell>Type</Table.Cell>
                                <Table.Cell>Description</Table.Cell>
                                <Table.Cell>Class Rating</Table.Cell>
                                <Table.Cell>Times</Table.Cell>
                                <Table.Cell>Days</Table.Cell>
                                <Table.Cell>Professor</Table.Cell>
                                <Table.Cell>Professor Rating</Table.Cell>
                                <Table.Cell>Courses Attributes</Table.Cell>
                                <Table.Cell></Table.Cell>
                            </Table.Row>
                        </Table.Header>
                        <Table.Body>
                            {this.renderOfferings(this.props.courseOfferings)}
                        </Table.Body>
                    </Table>
                </Modal.Content>
            </Modal>
        )
    }
}

export default CourseGroup