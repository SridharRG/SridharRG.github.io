## Local Community

Most of the contributions to OSM in Puducherry come from the members of the local **FOSS community** called **Free Software Hardware Movement** (aka FSHM). The community has been very active since 2011 and has its online presence on the Signal app. There is a dedicated group on [Signal](https://signal.org/download/) for OSM contributors.

- [OSM Puducherry - Signal Group](https://signal.group/#CjQKIIHiFUt_hroU6tnlGuD6qzWVCpM-t1zWNonz5yD-7pG5EhCr2u6OBTJ-gHXXkFBxFXT2)

## Public Infrastructure

Public infrastructure covers all amenities and utilities used by the general public and is 90% maintained by the government using public funds. Mapping these is important for policy advocacy to improve public infrastructure in Puducherry and make it a better and safer place to live.

## Road Network

- The **Public Works Department (PWD)** is responsible for road networks within the Union Territory.

## Street Lights

Street light mapping in Puducherry began in **August & September 2024**.

- [Street Light Map](https://sb12.github.io/OSMStreetLight/?#15/11.9354/79.8136) - Shows coverage of street lights mapped in Puducherry.
- The **Puducherry Electricity Department (PED)** and **Puducherry Smart City Development Ltd (PSCDL)** jointly install and maintain street lights throughout the Union Territory.

### How To Map Street Lights?

In Puducherry, it is becoming a **common practice to utilize existing electricity poles to mount street lamps**. Some locations have dedicated poles for street lamps, while others have street lights mounted on electricity poles.

**Note:** It is recommended to go out in the evening after the street lights have been turned on to clearly determine their operational status.

1. Install the [Every Door](https://every-door.app/) app on your smartphone.  
   - Apps like Organic Maps or OsmAnd are **not recommended** because live data is not loaded unless you enable **Live Updates** in OsmAnd. Using outdated data could lead to mapping already existing street lamps.
2. Enable GPS, walk along the street, stand below the street light, get a GPS fix, and add the street light to the map.
3. **Use appropriate tags:**
   - **Standalone street light pole:**  
     ```yaml
     highway=street_lamp
     ```
   - **Tall tower light (lighting mast):**  
     ```yaml
     man_made=mast
     tower:type=lighting
     ```
   - **Street light mounted on an electricity pole:**  
     ```yaml
     man_made=utility_pole
     utilities=power;street_lighting
     highway=street_lamp
     ```
4. **Add additional details regarding the lamp type, color of light, and operational status.**  
   - If you are unsure about the values, **do not add incorrect or assumed values**.
   - **Lamp type:**  
     ```yaml
     lamp_type=LED (or) sodium
     ```
     - **Puducherry Smart City Development Agency** is replacing sodium vapor lamps with LED lights.  
       - If you see a **white light**, it is 99% **LED**.  
       - If you see a **yellow light**, it is likely a **sodium vapor lamp**.  
       - Use only one value, not both.
     - References:  
       [Tender Document](http://pondicherrysmartcity.in/admin/tender/202203080528431530341737.pdf)  
       [The Hindu - LED Street Lights](https://www.thehindu.com/news/cities/puducherry/new-led-street-lights-commissioned-in-puducherry/article67821791.ece)
   - **Light color:**  
     ```yaml
     light:colour=white (or) yellow
     ```
   - **Operational status:**  
     ```yaml
     operational_status=operational (or) broken (or) needs_maintenance
     ```
     - If the **light is working properly**, use `operational`.
     - If the **light is not working**, use `broken`.
     - If the **light is working but needs maintenance**, use `needs_maintenance`.
   - **Date of last check:**  
     ```yaml
     check_date=yyyy-mm-dd
     ```
     - This represents when the street light's presence or operational status was last checked.
     - Enter the **date of your survey** in `YYYY-MM-DD` format.
