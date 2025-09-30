
# Mobile Surveillance System (MSS) — Workflows → Sub‑Workflows → Use Cases → Persona‑on‑the‑fly User Stories

_Source: “Technical Specifications — Mobile Surveillance System — Item 3.pdf”._

---

## Workflows

### WF‑1: Deploy & Set Up MSS at Observation Site
- **Entry Conditions:** Off‑road vehicle arrives at site; staffed by two operators; intended stationary operation up to 12 hours. 
- **Stages**
  1) Position vehicle; rotate operator seats; prepare operator & technical compartments (ergonomics, noise, lighting discipline).   
  2) Elevate EO head above roof; verify visual+audible interlocks; confirm parked/drive states. 
- **Exit Conditions:** EO head in observation position; compartments isolated; systems powered on.

### WF‑2: Observe, Detect & Recognize Targets
- **Entry Conditions:** EO head elevated; cameras operational. 
- **Stages**
  1) Day & night observation using daylight and thermovision cameras; maintain focus across FOV; auto FOV coupling enabled.   
  2) Stabilize video feed in real time; correct multi‑axis shake. 
- **Exit Conditions:** Targets observed per scenario; stabilized imagery available. 

### WF‑3: Range & Geolocate Targets
- **Entry Conditions:** Target observed; LRF armed.  
- **Stages**
  1) Measure range to first/near objects; show returns (up to 3) with accuracy and resolution; ensure eyesafe wavelength.   
  2) Overlay distance on video; place target on map with GPS/North; persist until next measure/save.   
- **Exit Conditions:** Target coordinates and range recorded on video/map. 

### WF‑4: Record, Retrieve & Transfer Data
- **Entry Conditions:** Sensors streaming to electronic unit (H.264/MPEG‑4/MJPEG), DVR available. 
- **Stages**
  1) Record stabilized imagery with coordinates/time; maintain ≥30 days retention & playback controls.   
  2) Transmit selected monitor image to local coordination centre over LTE/3G. 
- **Exit Conditions:** Evidence recorded and/or transmitted to command. 

### WF‑5: Communications over TETRA
- **Entry Conditions:** TETRA terminal installed and powered from vehicle battery. 
- **Stages**
  1) Voice/data services; individual, group, emergency, priority; talk‑group scanning and mutual authentication.   
  2) Security: AIE Class 1–3 (TEA2 Class 3), E2E crypto support; GPS (LIP/NMEA).   
- **Exit Conditions:** Reliable, secure comms with location telemetry. 

### WF‑6: Power Management & Safety
- **Entry Conditions:** Internal batteries, alternator, and optional 230V sources available. 
- **Stages**
  1) Automatic source switching; non‑disruptive charging; alarms for battery discharge and vehicle range.   
  2) Monitor power metrics; ensure gel batteries sized for 12‑hour duty cycle (+25% headroom). 
- **Exit Conditions:** Continuous 12‑hour stationary operation sustained. 

### WF‑7: Training & Documentation (Lifecycle)
- **Entry Conditions:** Delivery/commissioning.  
- **Stages**
  1) Deliver bilingual documentation (functional, install, O&M, wiring) per agreed scope.   
  2) Provide operator & technician training on identical equipment, day/night scenarios; certificates issued. 
- **Exit Conditions:** Staff certified; manuals accepted.

---

## Sub‑Workflows (Reusable)

- **SWF‑1: EO Head Elevation / Park / Safety Interlocks** — Elevate 1 m±10% above roof; warnings on start; roof de‑icing; overload protection; park for driving.   
- **SWF‑2: Thermovision Long‑Range Detection** — LWIR/MWIR, 640×480, FOV 0.8°–9°, Johnson: 15 km detect/6 km recog/3.5 km ID.   
- **SWF‑3: Video Stabilization** — Real‑time, multi‑axis, sub‑pixel precision.   
- **SWF‑4: DVR Evidence Handling** — Coordinates & time burned‑in; ≥30‑day retention; export via USB 3.0; parallel record/playback.   
- **SWF‑5: TETRA Secure Voice/Data** — Emergency/priority/scanning/auth; AIE (TEA2); GPS LIP/NMEA.   
- **SWF‑6: Power Source Orchestration** — Auto‑switch; metrics; gel batteries +25% headroom. 

---

## Use Cases

### UC‑1: Set Up Observation Post (WF‑1 Stage)
**Primary Actor:** Operator A (Driver/Tech)  
**Preconditions:** Off‑road site reached; 2‑person crew; stationary 12‑hour mission.   
**Triggers:** Patrol command to establish observation.  
**Main Flow:**  
1. Park and level; configure operator/technical compartments; noise/light discipline.   
2. Elevate EO head; confirm visual/acoustic warnings and park interlocks.   
3. Power‑on sensors; verify stabilization feed.   
**Postconditions:** MSS ready to observe.

### UC‑2: Perform Day/Night Surveillance (WF‑2 Stage)
**Primary Actor:** Operator B (Sensor)  
**Preconditions:** EO head elevated; cameras available.   
**Main Flow:**  
1. Select thermovision/daylight camera; maintain auto‑focus and linked FOVs.   
2. Scan sectors; automatically stabilize/optimize imagery.   
**Postconditions:** Continuous, stabilized observation achieved. 

### UC‑3: Range & Geolocate Target (WF‑3 Stage)
**Primary Actor:** Operator B (Sensor)  
**Main Flow:**  
1. Acquire range (first/near), with accuracy/resolution; confirm eyesafe.   
2. Overlay distance on video; mark on map with GPS/North.   
**Postconditions:** Target annotation present on both video and map. 

### UC‑4: Record Evidence (WF‑4 Stage)
**Primary Actor:** Operator A (DVR)  
**Main Flow:**  
1. Record selected monitor image with coordinates and real time; retain ≥30 days.   
2. Export snapshots/segments via USB 3.0 if requested.   
**Postconditions:** Evidence preserved; chain‑of‑custody supported.

### UC‑5: Transmit Live Feed to Coordination Centre (WF‑4 Stage)
**Primary Actor:** Operator A (Comms)  
**Main Flow:**  
1. Select LTE/3G; transmit complete image of chosen monitor.   
**Postconditions:** Command has situational awareness.

### UC‑6: Coordinate via TETRA (WF‑5 Stage)
**Primary Actor:** Any Operator  
**Main Flow:**  
1. Initiate individual/group/emergency calls; priority if needed; authenticate to infra.   
2. Operate with AIE (TEA2), E2E encryption; report GPS via LIP/NMEA.   
**Postconditions:** Secure voice/data link active.

### UC‑7: Manage Power for 12‑Hour Mission (WF‑6 Stage)
**Primary Actor:** Operator A (Power)  
**Main Flow:**  
1. Ensure internal batteries as main source; auto‑switching enabled; charging non‑disruptive.   
2. Monitor alarms and metrics; confirm capacity headroom.   
**Postconditions:** Uninterrupted operation maintained. 

### UC‑8: Conduct Day/Night Training Scenario (WF‑7 Stage)
**Primary Actor:** Trainer  
**Main Flow:**  
1. Train operators/techs on identical equipment; day/night use; issue certificates; provide bilingual docs.   
**Postconditions:** Crew certified; documentation delivered.

---

## User Stories (Persona‑on‑the‑fly)

### Story A — As **Mila Petrova (Border Ops Driver)**, I want to **set up the MSS and elevate the EO head safely** so that we can start a 12‑hour stationary surveillance shift without risking equipment damage.
- **Acceptance Criteria**
  - GIVEN a two‑person crew and a stationary 12‑hour mission, WHEN I park, prepare compartments, and elevate the head, THEN visual/acoustic warnings trigger and the head can be parked for driving. 

### Story B — As **Arben K., Sensor Operator**, I want to **conduct day/night observation with stabilized imagery** so that I can detect, recognize and track intrusions reliably.
- **Acceptance Criteria**
  - GIVEN daylight + thermovision cameras are available and linked for FOV/focus, WHEN I scan sectors, THEN imagery remains stabilized and useful for detection/recognition. 

### Story C — As **Sanja I., Sensor Operator**, I want to **range a target and pin it on the map** so that the team can coordinate interception.
- **Acceptance Criteria**
  - GIVEN a visible target, WHEN I measure distance with the eyesafe LRF and overlay it on video, AND place the point on the map, THEN coordinates persist until next measurement/save. 

### Story D — As **Ilir D., Evidence Tech**, I want to **record and export stabilized video with coordinates/time** so that incidents are auditable later.
- **Acceptance Criteria**
  - GIVEN the DVR is available, WHEN I record the selected monitor view with embedded coordinates/time and retain ≥30 days, THEN I can later export via USB 3.0. 

### Story E — As **Nina R., Comms Lead**, I want to **send the active monitor feed to the coordination centre over LTE/3G** so that command has live situational awareness.
- **Acceptance Criteria**
  - GIVEN connectivity is available, WHEN I choose LTE or 3G and transmit the selected monitor image, THEN the centre receives a complete picture. 

### Story F — As **Goran M., Radio Operator**, I want to **make secure group and emergency calls with GPS reporting** so that we coordinate safely under load.
- **Acceptance Criteria**
  - GIVEN the TETRA terminal is online, WHEN I place group/emergency calls with priority and mutual authentication, THEN AIE (TEA2) and GPS (LIP/NMEA) are applied. 

### Story G — As **Elena V., Power Monitor**, I want to **orchestrate battery/alternator/external power with alarms** so that the MSS runs continuously for the whole mission.
- **Acceptance Criteria**
  - GIVEN internal batteries are the main source, WHEN source switching and charging occur, THEN operation is uninterrupted and alarms/metrics are displayed; capacity ≥ mission load +25%. 

---

## Notes
- MSS will be operated by **two persons**; keep UI and procedures aligned to dual‑operator workflows. 
- **Thermovision performance** uses Johnson criteria (detect/recognize/ID) and must meet stated ranges; ensure vendor proof. 
- **Environmental and reliability** constraints (e.g., temperature, wind, humidity) apply across vehicle and EO subsystems (see §7.4 in source).

