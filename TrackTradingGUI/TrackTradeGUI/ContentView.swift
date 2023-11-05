//
//  ContentView.swift
//  TrackTradeGUI
//
//  Created by DanielYuan on 2023/11/5.
//

import SwiftUI
import PythonKit

let sys = Python.import("sys")


struct ContentView: View {
    var body: some View {
        NavigationView {
            List {
                NavigationLink(destination: AccountInfoView()) {
                    Label("Account Information", systemImage: "person.crop.circle")
                }
                NavigationLink(destination: TradingInterfaceView()) {
                    Label("Trading Interface", systemImage: "chart.bar")
                }
                NavigationLink(destination: MarketInfoView()) {
                    Label("Market Information", systemImage: "newspaper")
                }
                NavigationLink(destination: MainPage()) {
                    Label("Main Page", systemImage: "star")
                }
            }
            .listStyle(SidebarListStyle())
            .navigationTitle("TrackTrade")
            .toolbar {
                // Toolbar items here if needed
            }
            
            Text("Select a page")
                .font(.title)
                .foregroundColor(.secondary)
        }
    }
}

struct AccountInfoView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Asset Accounting")
                .font(.largeTitle)
                .fontWeight(.bold)

            // Additional content and logic for the account information page
        }
        .padding()
        .navigationTitle("Account Info")
    }
}

struct TradingInterfaceView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Trading")
                .font(.largeTitle)
                .fontWeight(.bold)

            // Additional content and logic for the trading interface page
        }
        .padding()
        .navigationTitle("Trading")
    }
}

struct MarketInfoView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Market Information")
                .font(.largeTitle)
                .fontWeight(.bold)

            // Additional content and logic for the market information page
        }
        .padding()
        .navigationTitle("Market Info")
    }
}

struct MainPage: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Log In")
                .font(.largeTitle)
                .fontWeight(.bold)

            // Additional content and logic for the market information page
        }
        .padding()
        .navigationTitle("Main Page")
    }
}


#Preview {
    ContentView()
}


