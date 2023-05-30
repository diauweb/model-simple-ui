"use strict";

Vue.createApp({
    data() {
        return {
            isLoading: false,
            imagePath: null,
            result: null
        }
    },
    methods: {
        async submit() {
            this.isLoading = true;
            const fileInput = this.$refs.fileInput;
            if (fileInput.files.length <= 0) {
                alert('No file is selected.');
                return;
            }
            
            this.isLoading = true;
            
            const file = fileInput.files[0];
            const form = new FormData();
            form.append('file', file);
            const resp = await fetch('/upload', {
                method: 'POST',
                body: form
            });
            
            const uploadResult = await resp.json();
            if (uploadResult.error) {
                alert(uploadResult);
                return;
            }
            
            this.imagePath = URL.createObjectURL(file);
            this.result = await (await fetch(`/check?handle=${uploadResult.file_handle}`)).json();
            this.isLoading = false;
        }
    },
    mounted() {

    },
}).mount('#app');