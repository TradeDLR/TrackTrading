//
//  File.swift
//  TrackTradeGUI
//
//  Created by DanielYuan on 2023/11/5.
//
import Foundation
import SwiftUI
import PythonKit

struct PythonInterface {
    static func printPythonVersion() {
        let sys = Python.import("sys")
        print("Python \(sys.version_info.major).\(sys.version_info.minor)")
        print("Python Version: \(sys.version)")
        print("Python Encoding: \(sys.getdefaultencoding().upper())")
    }
}

// Use this in an appropriate place, like in the main app struct or in response to a user action



struct CV: View {
    var body: some View {
        Text("Hello, World!")
            .onAppear {
                PythonInterface.printPythonVersion()
            }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        CV()
    }
}
