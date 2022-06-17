export interface CardComp {
    id: number;
    title: string;
    number: number;
  }

export const CardList: CardComp[] = [
    {
    id: 1,
    title: "Twitter",
    number: 50000,
    },
    {
    id: 2,
    title: "Facebook",
    number: 5425,
    },
    {
    id: 3,
    title: "Instagram",
    number: 0,
    },
    {
    id: 4,
    title: "Redit",
    number: 0,
    }
]

export function SomaLista(): number {
    let soma = 0;
    CardList.forEach(element => {
        soma += element.number;
    });
    return soma;
}
export function convertNumber(number) {
  return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}