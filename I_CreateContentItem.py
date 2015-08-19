'''
Created on Apr 14, 2015

@author: shurrey
'''
import logging
import sys
import suds
import random
 
from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
from suds.wsse import *    
from uuid import uuid1
from datetime import datetime
 
def getEntitlements():
    return(["Announcement.WS:createCourseAnnouncements",
                        "Announcement.WS:createOrgAnnouncements",
                        "Announcement.WS:createSystemAnnouncements",
                        "Announcement.WS:deleteCourseAnnouncements",
                        "Announcement.WS:deleteOrgAnnouncements",
                        "Announcement.WS:deleteSystemAnnouncements",
                        "Announcement.WS:getCourseAnnouncements",
                        "Announcement.WS:getOrgAnnouncements",
                        "Announcement.WS:getSystemAnnouncements",
                        "Announcement.WS:updateCourseAnnouncements",
                        "Announcement.WS:updateOrgAnnouncements",
                        "Announcement.WS:updateSystemAnnouncements",
                        "Calendar.WS:canUpdateCourseCalendarItem",
                        "Calendar.WS:canUpdateInstitutionCalendarItem",
                        "Calendar.WS:canUpdatePersonalCalendarItem",
                        "Calendar.WS:createCourseCalendarItem",
                        "Calendar.WS:createInstitutionCalendarItem",
                        "Calendar.WS:createPersonalCalendarItem",
                        "Calendar.WS:deleteCourseCalendarItem",
                        "Calendar.WS:deleteInstitutionCalendarItem",
                        "Calendar.WS:deletePersonalCalendarItem",
                        "Calendar.WS:getCalendarItem",
                        "Calendar.WS:saveCourseCalendarItem",
                        "Calendar.WS:saveInstitutionCalendarItem",
                        "Calendar.WS:savePersonalCalendarItem",
                        "Calendar.WS:updateCourseCalendarItem",
                        "Calendar.WS:updateInstitutionCalendarItem",
                        "Calendar.WS:updatePersonalCalendarItem",
                        "Content.WS:addContentFile",
                        "Content.WS:deleteContentFiles",
                        "Content.WS:deleteContents",
                        "Content.WS:deleteCourseTOCs",
                        "Content.WS:deleteLinks",
                        "Content.WS:getContentFiles",
                        "Content.WS:getFilteredContent",
                        "Content.WS:getFilteredCourseStatus",
                        "Content.WS:getLinksByReferredToType",
                        "Content.WS:getLinksByReferrerType",
                        "Content.WS:getReviewStatusByCourseId",
                        "Content.WS:getTOCsByCourseId",
                        "Content.WS:loadContent",
                        "Content.WS:removeContent",
                        "Content.WS:saveContent",
                        "Content.WS:saveContentsReviewed",
                        "Content.WS:saveCourseTOC",
                        "Content.WS:saveLink",
                        "Context.WS:emulateUser", 
                        "Context.WS:getMemberships", 
                        "Context.WS:getMyMemberships",
                        "Course.WS:changeCourseBatchUid",
                        "Course.WS:changeCourseCategoryBatchUid",
                        "Course.WS:changeCourseDataSourceId",
                        "Course.WS:changeOrgBatchUid",
                        "Course.WS:changeOrgCategoryBatchUid",
                        "Course.WS:changeOrgDataSourceId",
                        "Course.WS:createCourse",
                        "Course.WS:createOrg",
                        "Course.WS:deleteCartridge",
                        "Course.WS:deleteCourse",
                        "Course.WS:deleteCourseCategory",
                        "Course.WS:deleteCourseCategoryMembership",
                        "Course.WS:deleteGroup",
                        "Course.WS:deleteOrg",
                        "Course.WS:deleteOrgCategory",
                        "Course.WS:deleteOrgCategoryMembership",
                        "Course.WS:deleteStaffInfo",
                        "Course.WS:getAvailableGroupTools",
                        "Course.WS:getCartridge",
                        "Course.WS:getCategories",
                        "Course.WS:getCategoryMembership",
                        "Course.WS:getClassifications",
                        "Course.WS:getCourse",
                        "Course.WS:getGroup",
                        "Course.WS:getOrg",
                        "Course.WS:getStaffInfo",
                        "Course.WS:saveCartridge",
                        "Course.WS:saveCourse",
                        "Course.WS:saveCourseCategory",
                        "Course.WS:saveCourseCategoryMembership",
                        "Course.WS:saveGroup",
                        "Course.WS:saveOrgCategory",
                        "Course.WS:saveOrgCategoryMembership",
                        "Course.WS:saveStaffInfo",
                        "Course.WS:updateCourse",
                        "Course.WS:updateOrg",
                        "Course.WS:loadCoursesInTerm", 
                        "Course.WS:addCourseToTerm", 
                        "Course.WS:removeCourseFromTerm", 
                        "Course.WS:loadTerm", 
                        "Course.WS:loadTermByCourseId", 
                        "Course.WS:saveTerm", 
                        "Course.WS:removeTerm", 
                        "Course.WS:loadTerms", 
                        "Course.WS:loadTermsByName",
                        "CourseMembership.WS:deleteCourseMembership",
                        "CourseMembership.WS:deleteGroupMembership",
                        "CourseMembership.WS:getCourseMembership",
                        "CourseMembership.WS:getCourseRoles",
                        "CourseMembership.WS:getGroupMembership",
                        "CourseMembership.WS:saveCourseMembership",
                        "CourseMembership.WS:saveGroupMembership",
                        "Gradebook.WS:deleteAttempts",
                        "Gradebook.WS:deleteColumns",
                        "Gradebook.WS:deleteGradebookTypes",
                        "Gradebook.WS:deleteGrades",
                        "Gradebook.WS:deleteGradingSchemas",
                        "Gradebook.WS:getAttempts",
                        "Gradebook.WS:getGradebookColumns",
                        "Gradebook.WS:getGradebookTypes",
                        "Gradebook.WS:getGrades",
                        "Gradebook.WS:getGradingSchemas",
                        "Gradebook.WS:saveAttempts",
                        "Gradebook.WS:saveColumns",
                        "Gradebook.WS:saveGradebookTypes",
                        "Gradebook.WS:saveGrades",
                        "Gradebook.WS:saveGradingSchemas",
                        "Gradebook.WS:updateColumnAttribute",
                        "User.WS:changeUserBatchUid",
                        "User.WS:changeUserDataSourceId",
                        "User.WS:deleteAddressBookEntry",
                        "User.WS:deleteObserverAssociation",
                        "User.WS:deleteUser",
                        "User.WS:deleteUserByInstitutionRole",
                        "User.WS:getAddressBookEntry",
                        "User.WS:getInstitutionRoles",
                        "User.WS:getObservee",
                        "User.WS:getSystemRoles",
                        "User.WS:getUser",
                        "User.WS:getUserInstitutionRoles",
                        "User.WS:saveAddressBookEntry",
                        "User.WS:saveObserverAssociation",
                        "User.WS:saveUser",
                        "Util.WS:checkEntitlement",
                        "Util.WS:deleteSetting",
                        "Util.WS:getDataSources",
                        "Util.WS:loadSetting",
                        "Util.WS:saveSetting"])
    
def generate_nonce(length=8):
    """Generate pseudorandom number."""
    return ''.join([str(random.randint(0, 9)) for i in range(length)])
 
def createHeaders(action, username, password, endpoint):
    """Create the soap headers section of the XML to send to Blackboard Learn Web Service Endpoints"""
    
    # Namespaces
    xsd_ns = ('xsd', 'http://www.w3.org/2001/XMLSchema')
    wsu_ns = ('wsu',"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd")
    wsa_ns = ('wsa', 'http://schemas.xmlsoap.org/ws/2004/03/addressing')
    
    # Set the action. This is a string passed to this funtion and corresponds to the method being called
    # For example, if calling Context.WS.initialize(), this should be set to 'initialize'
    wsa_action = Element('Action', ns=wsa_ns).setText(action)
    
    # Each method requires a unique identifier. We are using Python's built-in uuid generation tool.
    wsa_uuid = Element('MessageID', ns=wsa_ns).setText('uuid:' + str(uuid1()))
    
    # Setting the replyTo address == to the SOAP role anonymous
    wsa_address = Element('Address', ns=wsa_ns).setText('http://schemas.xmlsoap.org/ws/2004/03/addressing/role/anonymous')
    wsa_replyTo = Element('ReplyTo', ns=wsa_ns).insert(wsa_address)
    
    # Setting the To element to the endpoint being called
    wsa_to = Element('To', ns=wsa_ns).setText(url_header + endpoint)
    
    # Generate the WS_Security headers necessary to authenticate to Learn's Web Services
    # To create a session, ContextWS.initialize() must first be called with username session and password no session.
    # This will return a session Id, which then becomes the password for subsequent calls.
    security = createWSSecurityHeader(username, password)
    
    # Return the soapheaders that can be added to the soap call
    return([wsa_action, wsa_uuid, wsa_replyTo, wsa_to, security])
    
def createWSSecurityHeader(username,password):
    """ 
        Generate the WS-Security headers for making Blackboard Web Service calls.
        
        SUDS comes with a WSSE header generation tool out of the box, but it does not offer
        the flexibility needed to properly authenticate to the Blackboard SOAP-based services.
        Thus, we are creating the necessary headers ourselves.
    """
    
    # Namespaces
    wsse = ('wsse', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd')
    wsu = ('wsu', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd')
    
 
    # Create Security Element
    security = Element('Security', ns=wsse)
    security.set('SOAP-ENV:mustUnderstand', '1')
    
    # Create UsernameToken, Username/Pass Element
    usernametoken = Element('UsernameToken', ns=wsse)
    
    # Add the wsu namespace to the Username Token. This is necessary for the created date to be included.
    # Also add a Security Token UUID to uniquely identify this username Token. This uses Python's built-in uuid generation tool.
    usernametoken.set('xmlns:wsu', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd')
    usernametoken.set('wsu:Id', 'SecurityToken-' + str(uuid1()))
    
    # Add the username token to the security header. This will always be 'session'
    uname = Element('Username', ns=wsse).setText(username)
    # Add the password element and set the type to 'PasswordText'.
    # This will be nosession on the initialize() call, and the returned sessionID on subsequent calls.
    passwd = Element('Password', ns=wsse).setText(password)
    passwd.set('Type', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText')
    # Add a nonce element to further uniquely identify this message.
    nonce = Element('Nonce', ns=wsse).setText(str(generate_nonce(24)))
    # Add the current time in UTC format.
    created = Element('Created', ns=wsu).setText(str(datetime.utcnow()))
 
    # Add Username, Password, Nonce, and Created elements to UsernameToken element.
    # Python inserts tags at the top, and Learn needs these in a specific order, so they are added in reverse order
    usernametoken.insert(created)
    usernametoken.insert(nonce)
    usernametoken.insert(passwd)
    usernametoken.insert(uname)
 
    # Insert the usernametoken into the wsse:security tag
    security.insert(usernametoken)
    
    # Create the timestamp in the wsu namespace. Set a unique id for this timestamp using Python's built-in user generation tool.
    timestamp = Element('Timestamp', ns=wsu)
    timestamp.set('wsu:Id', 'Timestamp-' + str(uuid1()))
    
    # Insert the timestamp into the wsse:security tag. This is done after usernametoken to insert before usernametoken in the subsequent XML
    security.insert(timestamp)
    
    # Return the security XML
    return security
    
 
if __name__ == '__main__':
    """
        This is the main class for the Blackboard Soap Web Services Python sample code.
        
        If I were to turn this into a production-level tool, much of this would be abstracted into more manageable chunks.
    """
    
    # If True, extra information will be printed to the console
    DEBUG = True;

    # If True, register tool and exit
    REGISTER = False; 

    # Set up logging. logging level is set to DEBUG on the suds tools in order to show you what's happening along the way. 
    # It will give you SOAP messages and responses, which will help you develop your own tool.
    #logging.basicConfig(level=logging.INFO)
    
    #logging.getLogger('suds.client').setLevel(logging.DEBUG)
    #logging.getLogger('suds.transport').setLevel(logging.DEBUG)
    #logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
    #logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
    
    # Necessary system-setting for handling large complex WSDLs
    sys.setrecursionlimit(10000)
    
    # Set up the base URL for Web Service endpoints
    protocol = 'https'
    server = 'localhost:9887'
    service_path = 'webapps/ws/services'
    url_header = protocol + "://" + server + "/" + service_path + "/"
    
    vendor_id = "bbdn"
    program_id = "Test"
    registration_password = ""
    tool_description = "Test registration for Liverpool"
    shared_password = "shared-password"
    
    # This is the pattern for the SUDS library to dynamically create your Web Service code.
    # There are caching capabilities so that you can avoid this overhead everytime your script runs.
    # I have included the code for each endpoint, although only the ones I need are uncommented.
    url = url_header + 'Context.WS?wsdl'
    contextWS = Client(url, autoblend=True)
    if DEBUG == True:
        print(contextWS)
        
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
    headers = []
    headers = createHeaders('initialize', "session", "nosession", 'Context.WS')
    
    # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
    contextWS.set_options(soapheaders=headers, port='Context.WSSOAP12port_https')
    
    # Initialize Context
    sessionId = contextWS.service.initialize()
    if DEBUG == True:
        print(sessionId)
    
    if REGISTER == True:    
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('registerTool', 'session', sessionId, 'Context.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        contextWS.set_options(soapheaders=headers, port='Context.WSSOAP12port_https')
        
        # Register Tool.
        registered = contextWS.factory.create("ns4:RegisterToolResultVO") 
        registered = contextWS.service.registerTool(vendor_id, program_id, registration_password, tool_description, shared_password, getEntitlements(), [])
        if DEBUG == True:
            print(registered)
    else:
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('loginTool', 'session', sessionId, 'Context.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        contextWS.set_options(soapheaders=headers, port='Context.WSSOAP12port_https')
        
        # Login as tool. 
        logged_in = contextWS.service.loginTool(shared_password, vendor_id, program_id, "", 3600)
        if DEBUG == True:
            print(logged_in)
    
        url = url_header + 'User.WS?wsdl'
        userWS = Client(url, autoblend=True)
        if DEBUG == True:
            print(userWS)
            
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('initializeUserWS', "session", sessionId, 'User.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        userWS.set_options(soapheaders=headers, port='User.WSSOAP12port_https')
        
        # Initialize User
        user_init = userWS.service.initializeUserWS(False)
        if DEBUG == True:
            print(user_init)
        
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('getUser', "session", sessionId, 'User.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        userWS.set_options(soapheaders=headers, port='User.WSSOAP12port_https')
     
        # Initialize Context
        user_filter = userWS.factory.create("ns4:UserFilter")
        user_filter.filterType = '6' 
        user_filter.name = 'administrator'
        
        user_vo = userWS.factory.create("ns4:UserVO")
        user_vo = userWS.service.getUser(user_filter)
        if DEBUG == True:
            print(user_vo)
            
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('saveUser', "session", sessionId, 'User.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        userWS.set_options(soapheaders=headers, port='User.WSSOAP12port_https')
     
        # Initialize Context
        new_user_vo = userWS.factory.create("ns4:UserVO")
        new_user_vo.name = "bob"
        new_user_vo.password = "iheartdevcon"
        new_user_vo.dataSourceId = "_1_1"
        new_user_vo.insRoles = ["STAFF"]
        new_user_vo.systemRoles = ["SYSTEM_ADMIN"]
        new_user_vo.userBatchUid = "bob"
        new_user_vo.isAvailable = "true"
        new_user_vo.extendedInfo.emailAddress = "bob@blackboard.com"
        
        print(new_user_vo)
        
        #user_id = userWS.service.saveUser([new_user_vo])
        #if DEBUG == True:
        #   print(user_id)
        user_id = "_37_1"
        
        url = url_header + 'Course.WS?wsdl'
        courseWS = Client(url, autoblend=True)
        if DEBUG == True:
            print(courseWS)
    
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('initializeCourseWS', "session", sessionId, 'Course.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        courseWS.set_options(soapheaders=headers, port='Course.WSSOAP12port_https')
        
        # Initialize Course
        course_init = courseWS.service.initializeCourseWS(False)
        if DEBUG == True:
            print(course_init)
        
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('saveCourse', "session", sessionId, 'Course.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        courseWS.set_options(soapheaders=headers, port='Course.WSSOAP12port_https')
     
        # Initialize Context
        new_course_vo = courseWS.factory.create("ns4:CourseVO")
        new_course_vo.name = "DevCon Course"
        new_course_vo.courseId = "COMPSCI-101"
        new_course_vo.available = "True"
        new_course_vo.description = "Test Course created for the SOAP Web Services Workshop."
        
        
        print(new_course_vo)
        
        #course_id = courseWS.service.saveCourse([new_course_vo])
        #if DEBUG == True:
        #    print(course_id)
        course_id = "_4_1"
    
        url = url_header + 'CourseMembership.WS?wsdl'
        courseMembershipWS = Client(url, autoblend=True)
        if DEBUG == True:
            print(courseMembershipWS)
            
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('initializeCourseMembershipWS', "session", sessionId, 'CourseMembership.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        courseMembershipWS.set_options(soapheaders=headers, port='CourseMembership.WSSOAP12port_https')
        
        # Initialize Course
        courseMembership_init = courseMembershipWS.service.initializeCourseMembershipWS(False)
        if DEBUG == True:
            print(courseMembership_init)
        
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('saveCourseMembership', "session", sessionId, 'CourseMembership.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        courseMembershipWS.set_options(soapheaders=headers, port='CourseMembership.WSSOAP12port_https')
     
        # Initialize Context
        new_courseMembership_vo = courseMembershipWS.factory.create("ns4:CourseMembershipVO")
        new_courseMembership_vo.courseId = course_id
        new_courseMembership_vo.userId = user_id
        new_courseMembership_vo.available = "True"
        new_courseMembership_vo.roleId = "P"        
        
        print(new_courseMembership_vo)
        
        #courseMembership_id = courseMembershipWS.service.saveCourseMembership(course_id, [new_courseMembership_vo])
        #if DEBUG == True:
        #    print(courseMembership_id)
        courseMembership_id = "_28_1"
        
        url = url_header + 'Announcement.WS?wsdl'
        announcementWS = Client(url, autoblend=True)
        if DEBUG == True:
            print(announcementWS)
            
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('initializeAnnouncementWS', "session", sessionId, 'Announcement.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        announcementWS.set_options(soapheaders=headers, port='Announcement.WSSOAP12port_https')
        
        # Initialize Course
        announcement_init = announcementWS.service.initializeAnnouncementWS(False)
        if DEBUG == True:
            print(announcement_init)
        
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('createCourseAnnouncements', "session", sessionId, 'Announcement.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        announcementWS.set_options(soapheaders=headers, port='Announcement.WSSOAP12port_https')
     
        # Initialize Context
        new_announcement_vo = announcementWS.factory.create("ns4:AnnouncementVO")
        new_announcement_vo.courseId = course_id
        new_announcement_vo.creatorUserId = user_id
        new_announcement_vo.title = "Welcome to the SOAP WS Workshop Course"
        new_announcement_vo.body = "This is a test announcement created by the Announcement Web Services.<br />Complete with <strong>HTML</strong>."        
        
        print(new_announcement_vo)
        
        #announcement_id = announcementWS.service.createCourseAnnouncements(course_id, [new_announcement_vo])
        #if DEBUG == True:
        #    print(announcement_id)
        announcement_id = "_3_1"
        
        url = url_header + 'Content.WS?wsdl'
        contentWS = Client(url, autoblend=True)
        if DEBUG == True:
            print(contentWS)
        
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('initializeVersion2ContentWS', "session", sessionId, 'Content.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        contentWS.set_options(soapheaders=headers, port='Content.WSSOAP12port_https')
        
        # Initialize Course
        content_init = contentWS.service.initializeVersion2ContentWS(False)
        if DEBUG == True:
            print(content_init)
        
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('getTOCsByCourseId', "session", sessionId, 'Content.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        contentWS.set_options(soapheaders=headers, port='Content.WSSOAP12port_https')
     
        course_toc_vo = contentWS.service.getTOCsByCourseId(course_id)
        if DEBUG == True:
            print(course_toc_vo)
            
        for toc_item in course_toc_vo:
            if toc_item.label == "Content":
                parent_id = toc_item.courseContentsId
                break
        
        print(parent_id)
        
        # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
        headers = []
        headers = createHeaders('saveContent', "session", sessionId, 'Content.WS')
        
        # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
        contentWS.set_options(soapheaders=headers, port='Content.WSSOAP12port_https')
     
        # Initialize Content
        new_content_vo = contentWS.factory.create("ns4:ContentVO")
        new_content_vo.contentHandler = "resource/x-bb-document"
        new_content_vo.available = "True"
        new_content_vo.parentId = parent_id
        new_content_vo.title = "SOAP WS Workshop Content Item"
        new_content_vo.body = "This is a test content item created by the Content Web Services.<br />Complete with <strong>HTML</strong>."        
        new_content_vo.externalId = "BbWsSoapWorkshopContent"
        
        print(new_content_vo)
        
        # Initialize Content
        course_id_vo = contentWS.factory.create("ns5:CourseIdVO")
        course_id_vo.externalId = course_id
        
        print(course_id_vo)
        
        
        content_id = contentWS.service.saveContent(course_id_vo, [new_content_vo])
        if DEBUG == True:
            print(content_id)
    
    # Initialize headers and then call createHeaders to generate the soap headers with WSSE bits.
    headers = []
    headers = createHeaders('logout', "session", sessionId, 'Context.WS')
    
    # Add Headers and WS-Security to client. Set port to default value, otherwise, you must add to service call
    contextWS.set_options(soapheaders=headers, port='Context.WSSOAP12port_https')
    
    # Initialize Context
    logged_out = contextWS.service.logout()
    if DEBUG == True:
        print(logged_out)