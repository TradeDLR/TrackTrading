# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/Cellar/cmake/3.27.7/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/Cellar/cmake/3.27.7/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/danielyuan/PycharmProjects/TrackTrading/frontend

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug

# Include any dependencies generated for this target.
include CMakeFiles/frontend.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/frontend.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/frontend.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/frontend.dir/flags.make

frontend_autogen/EWIEGA46WW/qrc_resources.cpp: /Users/danielyuan/PycharmProjects/TrackTrading/frontend/resources.qrc
frontend_autogen/EWIEGA46WW/qrc_resources.cpp: CMakeFiles/frontend_autogen.dir/AutoRcc_resources_EWIEGA46WW_Info.json
frontend_autogen/EWIEGA46WW/qrc_resources.cpp: /Users/danielyuan/PycharmProjects/TrackTrading/frontend/icons/cross.png
frontend_autogen/EWIEGA46WW/qrc_resources.cpp: /Users/danielyuan/PycharmProjects/TrackTrading/frontend/icons/burger.png
frontend_autogen/EWIEGA46WW/qrc_resources.cpp: /Users/danielyuan/PycharmProjects/TrackTrading/frontend/icons/arrow.png
frontend_autogen/EWIEGA46WW/qrc_resources.cpp: /opt/homebrew/Cellar/qt@5/5.15.10_1/bin/rcc
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Automatic RCC for resources.qrc"
	/opt/homebrew/Cellar/cmake/3.27.7/bin/cmake -E cmake_autorcc /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/CMakeFiles/frontend_autogen.dir/AutoRcc_resources_EWIEGA46WW_Info.json Debug

CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.o: CMakeFiles/frontend.dir/flags.make
CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.o: frontend_autogen/mocs_compilation.cpp
CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.o: CMakeFiles/frontend.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.o -MF CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.o.d -o CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.o -c /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/frontend_autogen/mocs_compilation.cpp

CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/frontend_autogen/mocs_compilation.cpp > CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.i

CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/frontend_autogen/mocs_compilation.cpp -o CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.s

CMakeFiles/frontend.dir/main.cpp.o: CMakeFiles/frontend.dir/flags.make
CMakeFiles/frontend.dir/main.cpp.o: /Users/danielyuan/PycharmProjects/TrackTrading/frontend/main.cpp
CMakeFiles/frontend.dir/main.cpp.o: CMakeFiles/frontend.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/frontend.dir/main.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/frontend.dir/main.cpp.o -MF CMakeFiles/frontend.dir/main.cpp.o.d -o CMakeFiles/frontend.dir/main.cpp.o -c /Users/danielyuan/PycharmProjects/TrackTrading/frontend/main.cpp

CMakeFiles/frontend.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/frontend.dir/main.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/danielyuan/PycharmProjects/TrackTrading/frontend/main.cpp > CMakeFiles/frontend.dir/main.cpp.i

CMakeFiles/frontend.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/frontend.dir/main.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/danielyuan/PycharmProjects/TrackTrading/frontend/main.cpp -o CMakeFiles/frontend.dir/main.cpp.s

CMakeFiles/frontend.dir/mainwindow.cpp.o: CMakeFiles/frontend.dir/flags.make
CMakeFiles/frontend.dir/mainwindow.cpp.o: /Users/danielyuan/PycharmProjects/TrackTrading/frontend/mainwindow.cpp
CMakeFiles/frontend.dir/mainwindow.cpp.o: CMakeFiles/frontend.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/frontend.dir/mainwindow.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/frontend.dir/mainwindow.cpp.o -MF CMakeFiles/frontend.dir/mainwindow.cpp.o.d -o CMakeFiles/frontend.dir/mainwindow.cpp.o -c /Users/danielyuan/PycharmProjects/TrackTrading/frontend/mainwindow.cpp

CMakeFiles/frontend.dir/mainwindow.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/frontend.dir/mainwindow.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/danielyuan/PycharmProjects/TrackTrading/frontend/mainwindow.cpp > CMakeFiles/frontend.dir/mainwindow.cpp.i

CMakeFiles/frontend.dir/mainwindow.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/frontend.dir/mainwindow.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/danielyuan/PycharmProjects/TrackTrading/frontend/mainwindow.cpp -o CMakeFiles/frontend.dir/mainwindow.cpp.s

CMakeFiles/frontend.dir/custombutton.cpp.o: CMakeFiles/frontend.dir/flags.make
CMakeFiles/frontend.dir/custombutton.cpp.o: /Users/danielyuan/PycharmProjects/TrackTrading/frontend/custombutton.cpp
CMakeFiles/frontend.dir/custombutton.cpp.o: CMakeFiles/frontend.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/frontend.dir/custombutton.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/frontend.dir/custombutton.cpp.o -MF CMakeFiles/frontend.dir/custombutton.cpp.o.d -o CMakeFiles/frontend.dir/custombutton.cpp.o -c /Users/danielyuan/PycharmProjects/TrackTrading/frontend/custombutton.cpp

CMakeFiles/frontend.dir/custombutton.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/frontend.dir/custombutton.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/danielyuan/PycharmProjects/TrackTrading/frontend/custombutton.cpp > CMakeFiles/frontend.dir/custombutton.cpp.i

CMakeFiles/frontend.dir/custombutton.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/frontend.dir/custombutton.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/danielyuan/PycharmProjects/TrackTrading/frontend/custombutton.cpp -o CMakeFiles/frontend.dir/custombutton.cpp.s

CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.o: CMakeFiles/frontend.dir/flags.make
CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.o: frontend_autogen/EWIEGA46WW/qrc_resources.cpp
CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.o: CMakeFiles/frontend.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.o -MF CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.o.d -o CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.o -c /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/frontend_autogen/EWIEGA46WW/qrc_resources.cpp

CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/frontend_autogen/EWIEGA46WW/qrc_resources.cpp > CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.i

CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/frontend_autogen/EWIEGA46WW/qrc_resources.cpp -o CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.s

# Object files for target frontend
frontend_OBJECTS = \
"CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.o" \
"CMakeFiles/frontend.dir/main.cpp.o" \
"CMakeFiles/frontend.dir/mainwindow.cpp.o" \
"CMakeFiles/frontend.dir/custombutton.cpp.o" \
"CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.o"

# External object files for target frontend
frontend_EXTERNAL_OBJECTS =

frontend.app/Contents/MacOS/frontend: CMakeFiles/frontend.dir/frontend_autogen/mocs_compilation.cpp.o
frontend.app/Contents/MacOS/frontend: CMakeFiles/frontend.dir/main.cpp.o
frontend.app/Contents/MacOS/frontend: CMakeFiles/frontend.dir/mainwindow.cpp.o
frontend.app/Contents/MacOS/frontend: CMakeFiles/frontend.dir/custombutton.cpp.o
frontend.app/Contents/MacOS/frontend: CMakeFiles/frontend.dir/frontend_autogen/EWIEGA46WW/qrc_resources.cpp.o
frontend.app/Contents/MacOS/frontend: CMakeFiles/frontend.dir/build.make
frontend.app/Contents/MacOS/frontend: /opt/homebrew/Cellar/qt@5/5.15.10_1/lib/QtWidgets.framework/QtWidgets
frontend.app/Contents/MacOS/frontend: /opt/homebrew/Cellar/qt@5/5.15.10_1/lib/QtGui.framework/QtGui
frontend.app/Contents/MacOS/frontend: /opt/homebrew/Cellar/qt@5/5.15.10_1/lib/QtCore.framework/QtCore
frontend.app/Contents/MacOS/frontend: CMakeFiles/frontend.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX executable frontend.app/Contents/MacOS/frontend"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/frontend.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/frontend.dir/build: frontend.app/Contents/MacOS/frontend
.PHONY : CMakeFiles/frontend.dir/build

CMakeFiles/frontend.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/frontend.dir/cmake_clean.cmake
.PHONY : CMakeFiles/frontend.dir/clean

CMakeFiles/frontend.dir/depend: frontend_autogen/EWIEGA46WW/qrc_resources.cpp
	cd /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/danielyuan/PycharmProjects/TrackTrading/frontend /Users/danielyuan/PycharmProjects/TrackTrading/frontend /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug /Users/danielyuan/PycharmProjects/TrackTrading/build-frontend-Desktop_arm_darwin_generic_mach_o_64bit-Debug/CMakeFiles/frontend.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/frontend.dir/depend

