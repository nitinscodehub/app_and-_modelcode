# GaitWatch - Parkinson's Early Detection App

## 1. Project Overview

**Project Name:** GaitWatch  
**Type:** Cross-platform Mobile Application (Flutter)  
**Core Functionality:** A health-tech application that performs gait analysis using smartphone sensors to detect early signs of Parkinson's disease through walk tests, displaying AI-based risk predictions.

---

## 2. Technology Stack & Choices

### Framework & Language
- **Flutter 3.41.1** (Stable)
- **Dart 3.11.0**

### Key Dependencies
- `flutter_riverpod` - State management
- `go_router` - Navigation & routing
- `fl_chart` - Gait trend visualization charts
- `shared_preferences` - Local storage for offline data
- `sensors_plus` - Accelerometer & gyroscope access
- `intl` - Date formatting
- `flutter_animate` - Smooth animations
- `pdf` - PDF report generation
- `path_provider` - File system access

### State Management
- **Riverpod** with proper provider architecture

### Architecture Pattern
- **Clean Architecture** with feature-based organization
- Separation: UI Layer → Domain Layer → Data Layer

---

## 3. Feature List

### Core Features
1. **Splash Screen** - Animated app launch with auto-navigation
2. **Onboarding Flow** - 3-slide introduction carousel
3. **Home Dashboard** - Welcome card, quick actions, last result summary
4. **Walk Test** - 30-second sensor-based gait test with countdown
5. **Result Display** - Risk score gauge, health status, action buttons
6. **History Log** - List of previous test results with date/scores
7. **Trend Graph** - Line chart showing gait risk over time
8. **Profile Management** - User health info (name, age, height, weight)
9. **Settings** - Dark mode toggle, notifications
10. **Reports** - PDF generation for test results
11. **Drawer Navigation** - Settings, About, Help, Privacy Policy

### Technical Features
- **Sensor Data Placeholder** - Accelerometer/Gyroscope data structure ready
- **ML API Service** - Mock prediction service for future backend integration
- **Offline Storage** - Local persistence of test history
- **Dark Mode** - Theme switching support
- **Responsive UI** - Adapts to different screen sizes
- **Elderly-Friendly** - Large buttons, high contrast, clear typography

---

## 4. UI/UX Design Direction

### Overall Visual Style
- **Medical-grade clinical interface** with modern Material Design 3
- Clean, card-based layouts with generous whitespace
- Rounded corners (16dp radius)
- Subtle elevation shadows
- Smooth page transitions and micro-animations

### Color Scheme
| Role | Light Mode | Dark Mode |
|------|------------|-----------|
| Primary | #0F62FE (Medical Blue) | #4B92FF |
| Secondary | #14B8A6 (Teal) | #2DD4BF |
| Background | #F8FAFC (Soft Gray) | #0F172A |
| Surface/Card | #FFFFFF | #1E293B |
| Text Primary | #1E293B | #F1F5F9 |
| Text Secondary | #64748B | #94A3B8 |
| Success | #22C55E | #4ADE80 |
| Warning | #F59E0B | #FBBF24 |
| Danger | #EF4444 | #F87171 |

### Layout Approach
- **Bottom Tab Navigation** with 4 tabs (Home, Walk Test, History, Profile)
- **Stack Navigation** for detail screens (Result, Graph, Reports)
- **Drawer Menu** for settings and information pages

### Typography
- Large, readable fonts (minimum 16sp body text)
- Bold headings for section titles
- High contrast ratios for accessibility

### Accessibility
- Minimum touch target: 48x48dp
- Clear visual feedback on interactions
- Support for system font scaling

---

## 5. App Structure

```
lib/
├── main.dart
├── core/
│   ├── theme/
│   ├── constants/
│   ├── utils/
│   └── routes/
├── features/
│   ├── splash/
│   ├── onboarding/
│   ├── home/
│   ├── walk_test/
│   ├── result/
│   ├── history/
│   ├── graph/
│   ├── profile/
│   └── settings/
├── services/
│   ├── gait_api_service.dart
│   ├── sensor_service.dart
│   └── storage_service.dart
├── models/
│   └── test_result.dart
└── widgets/
    ├── main_scaffold.dart
    └── reusable_widgets.dart
```
