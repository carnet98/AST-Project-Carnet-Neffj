# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dead/dce_instrumenter

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dead/dce_instrumenter/build

# Include any dependencies generated for this target.
include src/CMakeFiles/FIPCFGExtractor.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/CMakeFiles/FIPCFGExtractor.dir/compiler_depend.make

# Include the progress variables for this target.
include src/CMakeFiles/FIPCFGExtractor.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/FIPCFGExtractor.dir/flags.make

src/CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.o: src/CMakeFiles/FIPCFGExtractor.dir/flags.make
src/CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.o: ../src/FIPCFGExtractor.cpp
src/CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.o: src/CMakeFiles/FIPCFGExtractor.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/dead/dce_instrumenter/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.o"
	cd /home/dead/dce_instrumenter/build/src && /usr/sbin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.o -MF CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.o.d -o CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.o -c /home/dead/dce_instrumenter/src/FIPCFGExtractor.cpp

src/CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.i"
	cd /home/dead/dce_instrumenter/build/src && /usr/sbin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/dead/dce_instrumenter/src/FIPCFGExtractor.cpp > CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.i

src/CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.s"
	cd /home/dead/dce_instrumenter/build/src && /usr/sbin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/dead/dce_instrumenter/src/FIPCFGExtractor.cpp -o CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.s

# Object files for target FIPCFGExtractor
FIPCFGExtractor_OBJECTS = \
"CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.o"

# External object files for target FIPCFGExtractor
FIPCFGExtractor_EXTERNAL_OBJECTS =

lib/libFIPCFGExtractor.so: src/CMakeFiles/FIPCFGExtractor.dir/FIPCFGExtractor.cpp.o
lib/libFIPCFGExtractor.so: src/CMakeFiles/FIPCFGExtractor.dir/build.make
lib/libFIPCFGExtractor.so: src/CMakeFiles/FIPCFGExtractor.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/dead/dce_instrumenter/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared module ../lib/libFIPCFGExtractor.so"
	cd /home/dead/dce_instrumenter/build/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/FIPCFGExtractor.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/FIPCFGExtractor.dir/build: lib/libFIPCFGExtractor.so
.PHONY : src/CMakeFiles/FIPCFGExtractor.dir/build

src/CMakeFiles/FIPCFGExtractor.dir/clean:
	cd /home/dead/dce_instrumenter/build/src && $(CMAKE_COMMAND) -P CMakeFiles/FIPCFGExtractor.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/FIPCFGExtractor.dir/clean

src/CMakeFiles/FIPCFGExtractor.dir/depend:
	cd /home/dead/dce_instrumenter/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dead/dce_instrumenter /home/dead/dce_instrumenter/src /home/dead/dce_instrumenter/build /home/dead/dce_instrumenter/build/src /home/dead/dce_instrumenter/build/src/CMakeFiles/FIPCFGExtractor.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/FIPCFGExtractor.dir/depend

