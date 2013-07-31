import os
import os.path
import sys
import shutil

# Change before integration:
embPreviousName = "July_09_2013"
embTargetName = "July_27_2013"
# Change above before integration

embPreviousRootPath = os.path.join("D:\\Code\\Neutron\\3P\\EMB",embPreviousName)
embRootPath = os.path.join("D:\\Code\\Neutron\\3P\\EMB",embTargetName)

embSrc = "C:\\Code\\Materials\\Materials"
embProject = "C:\\Code\\Materials\\Materials\\source\\Solutions"
embOutput = "C:\\"
embAutoCopy = "\\\\eptbuild\\epstore\\3rdParties\\AutoCopy\\Neutron\\EMB"

srcIncludePath = "C:\\Code\\Materials\\Materials\\include"
srcPathBinaryDebug = "C:\\Code\\Materials\\Materials\\Toolkit\\binary\\bin\\win_vc10\\x64\\Debug"
srcPathBinaryRelease = "C:\\Code\\Materials\\Materials\\Toolkit\\binary\\bin\\win_vc10\\x64\\Release"
srcPathLibDebug = "C:\\Code\\Materials\\Materials\\Toolkit\\binary\\lib\\ExchangeMaterials\\win_vc10\\x64\\Debug"
srcPathLibRelease = "C:\\Code\\Materials\\Materials\\Toolkit\\binary\\lib\\ExchangeMaterials\\win_vc10\\x64\\Release"

destIncludePath = os.path.join(embRootPath,"WIN64\\include")
destPathBinaryDebug = os.path.join(embRootPath,"WIN64\\binary\\bin\\win_vc10\\x64\\Debug")
destPathBinaryRelease = os.path.join(embRootPath,"WIN64\\binary\\bin\\win_vc10\\x64\\Release")
destPathLibDebug = os.path.join(embRootPath,"WIN64\\binary\\lib\\ExchangeMaterials\\win_vc10\\x64\\Debug")
destPathLibRelease = os.path.join(embRootPath,"WIN64\\binary\\lib\\ExchangeMaterials\\win_vc10\\x64\\Release")

curWDir = os.getcwd()

def CleanDir( Dir ):
    if os.path.isdir( Dir ):
        paths = os.listdir( Dir )
        for path in paths:
            filePath = os.path.join( Dir, path )
            if os.path.isfile( filePath ):
                try:
                    os.remove( filePath )
                except os.error:
                    autoRun.exception( "remove %s error." %filePath )
            elif os.path.isdir( filePath ):
                shutil.rmtree(filePath,True)
    return True
	
def SyncCode() :
	print ("Pulling source code")
	os.chdir(embSrc)
	os.system("git pull")
	print ("Pull code finished.")

def BuildCode() :
	print("Clean Toolkit folder")
	os.chdir(embSrc)
	CleanDir(os.path.join(embSrc, "Toolkit"))
	
	print ("building debug.")
	os.chdir(curWDir)
	os.system( "cmd /k EMBBuild.bat {0}".format(os.path.join(embProject,"ExMaterials.sln")))


def CopyFiles() :
	print ("Copying files...")

	if not os.path.exists(embRootPath) :
		shutil.copytree(embPreviousRootPath, embRootPath)


	# Copy include folder:
	if os.path.exists(destIncludePath):
		shutil.rmtree(destIncludePath)
	shutil.copytree(srcIncludePath, destIncludePath)

	# Copy Libs
	if os.path.exists(destPathLibDebug):
		shutil.rmtree(destPathLibDebug)
	shutil.copytree(srcPathLibDebug, destPathLibDebug)
	
	if os.path.exists(destPathLibRelease):
		shutil.rmtree(destPathLibRelease)
	shutil.copytree(srcPathLibRelease, destPathLibRelease)
	
	# Copy bin to debug
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatSample.exe"), 			os.path.join(destPathBinaryDebug,"AdExMatSample.exe"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatSample.ilk"), 			os.path.join(destPathBinaryDebug,"AdExMatSample.ilk"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatSample.pdb"), 			os.path.join(destPathBinaryDebug,"AdExMatSample.pdb"))
			
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdAARToolkit.dll"), 			os.path.join(destPathBinaryDebug,"AdAARToolkit.dll"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdAARToolkit.ilk"), 			os.path.join(destPathBinaryDebug,"AdAARToolkit.ilk"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdAARToolkit.pdb"), 			os.path.join(destPathBinaryDebug,"AdAARToolkit.pdb"))
	
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExDbClient.dll"), 		os.path.join(destPathBinaryDebug,"AdExDbClient.dll"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExDbClient.ilk"), 		os.path.join(destPathBinaryDebug,"AdExDbClient.ilk"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExDbClient.pdb"), 		os.path.join(destPathBinaryDebug,"AdExDbClient.pdb"))
	
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatBuilder.exe"), 			os.path.join(destPathBinaryDebug,"AdExMatBuilder.exe"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatBuilder.ilk"), 			os.path.join(destPathBinaryDebug,"AdExMatBuilder.ilk"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatBuilder.pdb"), 			os.path.join(destPathBinaryDebug,"AdExMatBuilder.pdb"))
	
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatSample.exe"), 			os.path.join(destPathBinaryDebug,"AdExMatSample.exe"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatSample.ilk"), 			os.path.join(destPathBinaryDebug,"AdExMatSample.ilk"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatSample.pdb"), 			os.path.join(destPathBinaryDebug,"AdExMatSample.pdb"))
	
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatToolkit.dll"), 			os.path.join(destPathBinaryDebug,"AdExMatToolkit.dll"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatToolkit.ilk"), 			os.path.join(destPathBinaryDebug,"AdExMatToolkit.ilk"))
	shutil.copy(os.path.join(srcPathBinaryDebug,"AdExMatToolkit.pdb"), 			os.path.join(destPathBinaryDebug,"AdExMatToolkit.pdb"))
	
	shutil.copy(os.path.join(srcPathBinaryDebug,"Log4CPlusU_Ad_d1.dll"), 		os.path.join(destPathBinaryDebug,"Log4CPlusU_Ad_d1.dll"))
	
	# Copy bin to Release
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdExMatSample.exe"), 		os.path.join(destPathBinaryRelease,"AdExMatSample.exe"))
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdExMatSample.pdb"), 		os.path.join(destPathBinaryRelease,"AdExMatSample.pdb"))
			
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdAARToolkit.dll"), 		os.path.join(destPathBinaryRelease,"AdAARToolkit.dll"))
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdAARToolkit.pdb"), 		os.path.join(destPathBinaryRelease,"AdAARToolkit.pdb"))
	
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdExDbClient.dll"), 		os.path.join(destPathBinaryRelease,"AdExDbClient.dll"))
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdExDbClient.pdb"), 		os.path.join(destPathBinaryRelease,"AdExDbClient.pdb"))
	
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdExMatBuilder.exe"), 		os.path.join(destPathBinaryRelease,"AdExMatBuilder.exe"))
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdExMatBuilder.pdb"), 		os.path.join(destPathBinaryRelease,"AdExMatBuilder.pdb"))
	
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdExMatSample.exe"), 		os.path.join(destPathBinaryRelease,"AdExMatSample.exe"))	
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdExMatSample.pdb"), 		os.path.join(destPathBinaryRelease,"AdExMatSample.pdb"))
	
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdExMatToolkit.dll"), 		os.path.join(destPathBinaryRelease,"AdExMatToolkit.dll"))
	shutil.copy(os.path.join(srcPathBinaryRelease,"AdExMatToolkit.pdb"), 		os.path.join(destPathBinaryRelease,"AdExMatToolkit.pdb"))
	
	shutil.copy(os.path.join(srcPathBinaryRelease,"Log4CPlusU_Ad_1.dll"), 		os.path.join(destPathBinaryRelease,"Log4CPlusU_Ad_1.dll"))
	



	print ("All files copied.")

def ArchiveFiles() :
	print ("Starting to archiving...")
	cmd7z= "D:\\Code\\Neutron\\main\\src\\Build\\Windows\\Tools\\7zip\\7z.exe a -r {0} {1}".format(os.path.join(curWDir,"WIN64.7z"),os.path.join(embRootPath,"WIN64\\*"))
	os.system(cmd7z);
	print ("Archive finished.")

def UploadToServer():
	print ("start uploading...")
	newEMBFolder = os.path.join(embAutoCopy,embTargetName)
	
	if not os.path.exists(newEMBFolder):
		os.mkdir(newEMBFolder) 
	
	shutil.copy(os.path.join(curWDir,"WIN64.7z"),os.path.join(newEMBFolder,"WIN64.7z")) 
	print ("Upload finished.")




# Step 1: Sync code from git.
SyncCode()

# Step 2: Build code. Debug/Release
BuildCode()

# Step 3: Copy files.
CopyFiles()

# Step 4: Archive to Mac64.7z
ArchiveFiles()

# Step 5: Upload to //eptbuild/eptstore/thirdparties/autocopy
UploadToServer()

