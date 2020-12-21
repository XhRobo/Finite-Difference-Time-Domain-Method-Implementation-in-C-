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
renderView1.CameraPosition = [106.56447055019734, 80.33512577261659, 196.27235493244385]
renderView1.CameraFocalPoint = [24.49999999999999, 24.499999999999996, 24.499999999999996]
renderView1.CameraViewUp = [-0.09048418652094622, 0.9590195999498532, -0.26850329402386547]
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
hcsv = CSVReader(FileName=['C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.4', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.5', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.6', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.7', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.8', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.9', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.10', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.11', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.12', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.13', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.14', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.15', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.16', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.17', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.18', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.19', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.20', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.21', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.22', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.23', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.24', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.25', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.26', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.27', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.28', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.29', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.30', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.31', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.32', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.33', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.34', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.35', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.36', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.37', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.38', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.39', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.40', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.41', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.42', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.43', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.44', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.45', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.46', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.47', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.48', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.49', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.50', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.51', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.52', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.53', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.54', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.55', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.56', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.57', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.58', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.59', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.60', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.61', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.62', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.63', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.64', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.65', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.66', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.67', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.68', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.69', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.70', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.71', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.72', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.73', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.74', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.75', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.76', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.77', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.78', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.79', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.80', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.81', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.82', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.83', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.84', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.85', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.86', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.87', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.88', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.89', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.90', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.91', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.92', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.93', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.94', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.95', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.96', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.97', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.98', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.99', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.100', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.101', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.102', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.103', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.104', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.105', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.106', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.107', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.108', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.109', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.110', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.111', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.112', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.113', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.114', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.115', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.116', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.117', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.118', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.119', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.120', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.121', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.122', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.123', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.124', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.125', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.126', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.127', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.128', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.129', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.130', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.131', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.132', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.133', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.134', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.135', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.136', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.137', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.138', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.139', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.140', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.141', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.142', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.143', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.144', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.145', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.146', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.147', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.148', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.149', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.150', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.151', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.152', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.153', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.154', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.155', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.156', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.157', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.158', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.159', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.160', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.161', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.162', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.163', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.164', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.165', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.166', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.167', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.168', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.169', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.170', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.171', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.172', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.173', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.174', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.175', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.176', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.177', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.178', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.179', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.180', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.181', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.182', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.183', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.184', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.185', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.186', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.187', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.188', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.189', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.190', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.191', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.192', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.193', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.194', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.195', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.196', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.197', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.198', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.199', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.0', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.1', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.2', 'C:/Users/xhoni/OneDrive/Desktop/Master Thesis/trunk/FDTD3D/Out/H/H.csv.3'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=hcsv)
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
glyph1.ScaleFactor = 1000000000.0
glyph1.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tableToPoints1
tableToPoints1Display = Show(tableToPoints1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tableToPoints1Display.Representation = 'Surface'
tableToPoints1Display.ColorArrayName = [None, '']
tableToPoints1Display.OSPRayScaleArray = 'Vx'
tableToPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tableToPoints1Display.SelectOrientationVectors = 'None'
tableToPoints1Display.ScaleFactor = 4.9
tableToPoints1Display.SelectScaleArray = 'None'
tableToPoints1Display.GlyphType = 'Arrow'
tableToPoints1Display.GlyphTableIndexArray = 'None'
tableToPoints1Display.GaussianRadius = 0.245
tableToPoints1Display.SetScaleArray = ['POINTS', 'Vx']
tableToPoints1Display.ScaleTransferFunction = 'PiecewiseFunction'
tableToPoints1Display.OpacityArray = ['POINTS', 'Vx']
tableToPoints1Display.OpacityTransferFunction = 'PiecewiseFunction'
tableToPoints1Display.DataAxesGrid = 'GridAxesRepresentation'
tableToPoints1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tableToPoints1Display.ScaleTransferFunction.Points = [-4.86907e-25, 0.0, 0.5, 0.0, 4.05756e-25, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tableToPoints1Display.OpacityTransferFunction.Points = [-4.86907e-25, 0.0, 0.5, 0.0, 4.05756e-25, 1.0, 0.5, 0.0]

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
calculator1Display.ScaleTransferFunction.Points = [-4.86907e-25, 0.0, 0.5, 0.0, 4.05756e-25, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-4.86907e-25, 0.0, 0.5, 0.0, 4.05756e-25, 1.0, 0.5, 0.0]

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
glyph1Display.ScaleTransferFunction.Points = [-1.21727e-25, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-1.21727e-25, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(tableToPoints1, renderView1)

# hide data in view
Hide(calculator1, renderView1)

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(glyph1)
# ----------------------------------------------------------------