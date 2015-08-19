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
 
if __name__ == '__main__':
    """
        This is the main class for the Blackboard Soap Web Services Python sample code.
        
        If I were to turn this into a production-level tool, much of this would be abstracted into more manageable chunks.
    """
    
    # If True, extra information will be printed to the console
    DEBUG = True;
    
    # If True, register tool and exit
    REGISTER = True;
 
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