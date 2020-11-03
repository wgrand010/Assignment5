# keyRotationWithUI.py

import maya.cmds as cmds
import functools

def createUI( pWindowTitle, pApplyCallback ):
    
    windowID = 'myWindowID'
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
        
    cmds.window( windowID, title=pWindowTitle, sizeable=True, resizeToFitChildren=True )
    
    cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[ (1,200), (2,200) ], columnOffset=[ (1,'right',3) ] )
    
    cmds.text( label='Choose Object to be scattered from: ' )
    
    startTimeField =cmds.button(label = object)
    
    cmds.text( label='Choose Object to be scattered to:' )
    
    targetAttributeField = cmds.button(label = object)
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    
    cmds.separator( h=10, style='none' )
    
    cmds.button( label='Scatter', command=functools.partial( pApplyCallback,
                                                  startTimeField,

                                                  targetAttributeField ) )

    cmds.showWindow()

def keyFullRotation( pObjectName, pStartTime, pEndTime, pTargetAttribute ):
    
    cmds.cutKey( pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute )
    
    cmds.setKeyframe( pObjectName, time=pStartTime, attribute=pTargetAttribute, value=0 )
    
    cmds.setKeyframe( pObjectName, time=pEndTime, attribute=pTargetAttribute, value=360 )
    
    cmds.selectKey( pObjectName, time=(pStartTime, pEndTime), attribute=pTargetAttribute, keyframe=True )
    
    cmds.keyTangent( inTangentType='linear', outTangentType='linear' )
    
    
def applyCallback( pStartTimeField, pEndTimeField, pTargetAttributeField, *pArgs ):
    
    # print 'Apply button pressed.'
    
    startTime = cmds.intField( pStartTimeField, query=True, value=True )
    
    endTime = cmds.intField( pEndTimeField, query=True, value=True )
    
    targetAttribute = cmds.textField( pTargetAttributeField, query=True, text=True )
    
    print 'Start Time: %s' % ( startTime )
    print 'End Time: %s' % ( endTime )
    print 'Attribute: %s' % ( targetAttribute )
    
    selectionList = cmds.ls( selection=True, type='transform' )
    
    for objectName in selectionList:
        
        keyFullRotation( objectName, startTime, endTime, targetAttribute )
    
createUI( 'My Title', applyCallback )
    
    
    
    
    
    
    
    
    
    