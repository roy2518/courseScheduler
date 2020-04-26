import React, { Fragment } from 'react'
import { Modal, Table, Image } from 'semantic-ui-react'

class ValidationPopup extends React.Component {

    validateSchedule = (courseOfferings) => {
        if (courseOfferings.length === 0) {
            return (true)
        }

        let first = courseOfferings[0]
        let rest = courseOfferings.slice(1)
        for (let courseOffering of rest) {
            for (let day of Object.keys(courseOffering.days)) {
                //long line incoming
                if (first.days[day] === true &&
                    courseOffering.days[day] === true &&
                    (
                        ((parseInt(first.start_time.replace(/:/g, "")) <= parseInt(courseOffering.start_time.replace(/:/g, ""))) && (parseInt(first.end_time.replace(/:/g, "")) > parseInt(courseOffering.start_time.replace(/:/g, "")))) ||
                        ((parseInt(first.start_time.replace(/:/g, "")) < parseInt(courseOffering.end_time.replace(/:/g, ""))) && (parseInt(first.start_time.replace(/:/g, "")) >= parseInt(courseOffering.start_time.replace(/:/g, ""))))
                    )
                ) {
                    return ([first, courseOffering])
                }
            }
        }
        return (this.validateSchedule(rest))
    }

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
                    <Table.Cell>{Object.entries(offering.attributes).map(attr => { if (attr[1]) { return `${attr[0].toUpperCase()} ` } })}</Table.Cell>
                </Table.Row>
            )
        })
    }

    generateContent = () => {
        if (this.props.courses.length === 0) {
            return (
                <Fragment>
                    <Modal.Header>Empty Schedule!</Modal.Header>
                    <Modal.Content>
                        <Image src={`${process.env.PUBLIC_URL}/no.png`} centered size='small' style={{ border: "6px solid #F06990" }} />
                        <div style={{ fontSize: 'large' }}>
                            I, Jerry, have noticed your schedule contains not even a single course!
                            Please come back after adding some courses!
                        </div>
                    </Modal.Content>
                </Fragment>

            )
        } else if (this.props.courses.filter(course => course.type === 'lec').length > 5) {
            return (
                <Fragment>
                    <Modal.Header>Too Many Courses!</Modal.Header>
                    <Modal.Content>
                        <Image src={`${process.env.PUBLIC_URL}/no.png`} centered size='small' style={{ border: "6px solid #F06990" }} />
                        <div style={{ fontSize: 'large' }}>
                            I, Jerry, observe that you have too many courses in your schedule!
                            Keep in mind that you cannot take more than FIVE full-credit classes!
                        </div>
                    </Modal.Content>
                </Fragment>
            )
        } else if (this.validateSchedule(this.props.courses) === true) {
            return (
                <Fragment>
                    <Modal.Header>All Clear!</Modal.Header>
                    <Modal.Content>
                        <Image src={`${process.env.PUBLIC_URL}/yes.png`} centered size='small' style={{ border: "6px solid #F06990" }} />
                        <div style={{ fontSize: 'large' }}>
                        I, Jerry, do not see any problems with your schedule!
                        Hope your next semester is JERRY good!
                        </div>
                    </Modal.Content>
                </Fragment>
            )
        } else if (this.validateSchedule(this.props.courses) !== true) {
            let conflict = this.validateSchedule(this.props.courses)
            return (
                <Fragment>
                    <Modal.Header>Schedule Conflict!</Modal.Header>
                    <Modal.Content>
                    <Image src={`${process.env.PUBLIC_URL}/no.png`} centered size='small' style={{ border: "6px solid #F06990" }} />
                        <div style={{ fontSize: 'large' }}>
                        I, Jerry, have found a conflict in your schedule!
                        Take a look below to see which two courses caused the conflict.
                        </div>
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
                                </Table.Row>
                            </Table.Header>
                            <Table.Body>
                                {this.renderOfferings(conflict)}
                            </Table.Body>
                        </Table>
                    </Modal.Content>
                </Fragment>
            )
        }
    }

    render() {

        return (
            <Modal trigger={this.props.trigger}>
                {this.generateContent()}
            </Modal>
        )
    }
}

export default ValidationPopup