$(function(){
    $("#tabEdit").FullTable({
        "alwaysCreating": true,
        "selectable": true,
        "fields":{
            "tipo": {
                "options": [
                    {
                        "title": "Receita",
                        "value": 1
                    },
                    {
                        "title": "Despesas",
                        "value": 2
                    }
                ],
                "mandatory": true,
                "placeholder": "Select one",
                "errors": {
                    "mandatory": "O Tipo de Lançamento é obrigatório."
                }
            },
            "categoria": {
                "mandatory": true,
                "errors": {
                    "mandatory": "A Categoria é obrigatória."
                }
            },
            "descricao": {
                "mandatory": true,
                "errors": {
                    "mandatory": "A Descrição não pode ser vazia."
                }
            },
            "valor": {
                "mandatory": true,
                "errors": {
                    "mandatory": "O Valor é obrigatória."
                }
            },
            "data_pag":{
                "mandatory": true
            },
            "data_acu": {
                "mandatory": true
            }
        }
    })
});