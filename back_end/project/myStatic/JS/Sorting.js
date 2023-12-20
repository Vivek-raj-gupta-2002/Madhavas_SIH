
    // Sample API endpoint for fetching data (replace with your actual API endpoint)
    const apiEndpoint = '/institute/api/getClg';
    const institute   = document.querySelector("#id_institute");
    const state   = document.querySelector("#id_state");
    


    async function fetchData(query) {
      try {
        const response = await fetch(`${apiEndpoint}/all`);
        const data = await response.json();
        let  states  = JSON.parse(data.data)
        console.log(states)
        console.log( institute);

        let  html = '';
        states.forEach((item =>{
        
            if ( item.State == query){
                html += `<option value="${item['College Name']}" >${item['College Name']} </option >`
            }
        
        }))

        console.log(html)
        institute.innerHTML= html;
        
        return data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    function handleInput(e) {
        console.log(e)
      const selectInput = document.querySelector('#id_institute');
      const query = selectInput.value.trim();

      if (!query) {
        // Clear options if the input is empty
        selectInput.innerHTML = 'id_institute';
        return;
      }

      // Fetch data based on the input query
      fetchData(query).then(data => {
        // Sort data alphabetically by name
        console.log(data);
        const sortedData = data.sort((a, b) => a.name.localeCompare(b.name));

        // Clear existing options
        selectInput.innerHTML = '';

        // Add sorted options to the select input
        sortedData.forEach(item => {
          const option = document.createElement('option');
          option.value = item.id;  // Assuming 'id' is the primary key of the College model
          option.text = item.name;  // Replace 'name' with the actual field you want to display
          selectInput.appendChild(option);
        });
      });
    }
    console.log(document.querySelector('#id_institute'));

    // Attach the handleInput function to the select input's change event
    document.querySelector('#id_institute').addEventListener('change', handleInput);
  fetchData('Andhra Pradesh');

  state.addEventListener('change' , (e)=>{
    fetchData(e.target.value)
  })