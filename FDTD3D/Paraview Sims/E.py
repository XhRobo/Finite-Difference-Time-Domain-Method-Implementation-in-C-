# state file generated using paraview version 5.8.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1461, 631]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [24.5, 24.5, 24.5]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [103.46165516801267, 101.25584070471393, 189.51963048863647]
renderView1.CameraFocalPoint = [24.499999999999982, 24.49999999999999, 24.5]
renderView1.CameraViewUp = [-0.09544785994715148, 0.9192596286193867, -0.3819050159687042]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 42.4352447854375
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.Visibility = 1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
ecsv = CSVReader(FileName=['C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.4', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.5', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.6', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.7', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.8', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.9', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.10', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.11', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.12', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.13', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.14', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.15', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.16', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.17', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.18', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.19', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.20', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.21', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.22', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.23', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.24', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.25', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.26', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.27', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.28', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.29', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.30', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.31', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.32', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.33', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.34', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.35', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.36', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.37', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.38', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.39', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.40', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.41', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.42', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.43', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.44', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.45', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.46', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.47', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.48', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.49', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.50', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.51', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.52', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.53', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.54', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.55', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.56', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.57', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.58', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.59', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.60', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.61', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.62', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.63', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.64', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.65', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.66', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.67', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.68', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.69', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.70', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.71', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.72', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.73', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.74', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.75', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.76', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.77', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.78', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.79', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.80', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.81', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.82', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.83', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.84', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.85', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.86', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.87', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.88', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.89', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.90', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.91', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.92', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.93', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.94', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.95', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.96', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.97', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.98', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.99', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.100', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.101', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.102', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.103', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.104', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.105', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.106', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.107', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.108', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.109', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.110', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.111', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.112', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.113', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.114', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.115', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.116', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.117', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.118', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.119', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.120', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.121', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.122', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.123', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.124', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.125', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.126', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.127', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.128', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.129', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.130', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.131', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.132', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.133', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.134', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.135', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.136', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.137', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.138', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.139', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.140', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.141', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.142', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.143', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.144', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.145', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.146', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.147', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.148', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.149', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.150', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.151', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.152', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.153', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.154', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.155', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.156', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.157', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.158', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.159', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.160', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.161', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.162', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.163', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.164', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.165', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.166', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.167', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.168', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.169', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.170', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.171', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.172', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.173', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.174', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.175', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.176', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.177', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.178', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.179', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.180', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.181', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.182', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.183', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.184', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.185', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.186', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.187', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.188', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.189', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.190', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.191', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.192', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.193', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.194', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.195', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.196', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.197', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.198', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.199', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.0', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.1', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.2', 'C:/Users/xhoni/eclipse-workspace/FDTD3D/Out/E/E.csv.3'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=ecsv)
tableToPoints1.XColumn = 'x'
tableToPoints1.YColumn = 'y'
tableToPoints1.ZColumn = 'z'
tableToPoints1.KeepAllDataArrays = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=tableToPoints1)
calculator1.Function = 'iHat*Vx+jHat*Vy+kHat*Vz'

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Line')
glyph1.OrientationArray = ['POINTS', 'Result']
glyph1.ScaleArray = ['POINTS', 'Result']
glyph1.ScaleFactor = 4000000.0
glyph1.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = [None, '']
calculator1Display.OSPRayScaleArray = 'Result'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'Result'
calculator1Display.ScaleFactor = 4.9
calculator1Display.SelectScaleArray = 'None'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'None'
calculator1Display.GaussianRadius = 0.245
calculator1Display.SetScaleArray = ['POINTS', 'Result']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'Result']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-2.888e-06, 0.0, 0.5, 0.0, 2.1058999999999996e-06, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-2.888e-06, 0.0, 0.5, 0.0, 2.1058999999999996e-06, 1.0, 0.5, 0.0]

# show data from glyph1
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = [None, '']
glyph1Display.OSPRayScaleArray = 'Vx'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 5.390000152587891
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.2695000076293945
glyph1Display.SetScaleArray = ['POINTS', 'Vx']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'Vx']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-8.63536e-08, 0.0, 0.5, 0.0, 7.407409999999998e-08, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-8.63536e-08, 0.0, 0.5, 0.0, 7.407409999999998e-08, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(glyph1)
# ----------------------------------------------------------------