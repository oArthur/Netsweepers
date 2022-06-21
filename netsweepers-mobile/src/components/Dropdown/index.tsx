import React from 'react';

import SelectDropdown from 'react-native-select-dropdown';
import { MaterialIcons } from '@expo/vector-icons';
import { Styles } from './style';


const months = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro", "Todos"];

const getNumberMonth = () => {
    const date = new Date();
    const month = date.getMonth();
    return month;
}
export default function Dropdown() {
    return (
        <SelectDropdown
            data={months}
            onSelect={(selectedItem, index) => {
                console.log(selectedItem, index)
            }}
            defaultValue={getNumberMonth()}
            defaultButtonText={months[getNumberMonth()]}
            renderDropdownIcon={() => <MaterialIcons name="arrow-drop-down" size={30} color="#fff" />}
            buttonStyle={Styles.dropdown1BtnStyle}
            dropdownStyle={Styles.dropdown1DropdownStyle}
            rowStyle={Styles.dropdown1RowStyle}
            rowTextStyle={Styles.dropdown1RowTxtStyle}
            buttonTextStyle={Styles.dropdown1BtnTxtStyle}
            buttonTextAfterSelection={(selectedItem, index) => {
                // text represented after item is selected
                // if data array is an array of objects then return selectedItem.property to render after item is selected
                return selectedItem
            }}
            rowTextForSelection={(item, index) => {
                // text represented for each item in dropdown
                // if data array is an array of objects then return item.property to represent item in dropdown
                return item
            }}
        />
    );
}